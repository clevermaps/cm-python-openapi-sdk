# clients/load_data_client.py
import os
import requests
import logging
import time
import gzip
from typing import Optional
from . import BaseClient

logger = logging.getLogger(__name__)


class LoadDataClient(BaseClient):
    """
    High-level client for data loading operations.
    
    Provides convenient methods for:
    - Uploading CSV files (single-part and multipart)
    - Automatic file splitting for large files
    - Job monitoring and status tracking
    """
    
    def __init__(self, api_token: str, host: Optional[str] = None, chunk_size: int = 20 * 1024 * 1024):
        """
        Initialize the LoadData client.
        
        Args:
            api_token: API access token (required)
            host: API host URL (optional, uses default if not provided)
            chunk_size: Size in bytes for multipart upload chunks (default: 50MB)
        """
        super().__init__(api_token, host)
        self.chunk_size = chunk_size
        self.target_part_size = 20 * 1024 * 1024  # 20MB target part size
        self.content_type = 'text/csv; charset=utf-8'
    
    def upload_data(
        self, 
        project_id: str, 
        csv_file_path: str, 
        dataset_name: str,
        poll_job: bool = True,
        poll_interval: int = 5
    ):
        """
        Upload a CSV file to the platform.
        
        Automatically chooses between single-part and multipart upload
        based on file size.
        
        Args:
            project_id: The ID of the project to upload to
            csv_file_path: Path to the CSV file
            dataset_name: Name of the dataset
            poll_job: Whether to wait for job completion (default: True)
            poll_interval: Seconds between status checks if polling (default: 5)
        
        Returns:
            Job response object
        
        Raises:
            FileNotFoundError: If the CSV file doesn't exist
            Exception: For API-related errors
        """
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"CSV file not found: {csv_file_path}")
        
        file_size = os.path.getsize(csv_file_path)
        logger.debug(f"File size: {file_size} bytes")
        
        # Choose upload method based on file size
        if file_size <= self.chunk_size:
            logger.debug("Using single-part upload")
            job_response = self._single_part_upload(project_id, csv_file_path, dataset_name)
        else:
            # Calculate number of parts based on target part size
            parts = (file_size + self.target_part_size - 1) // self.target_part_size
            logger.debug(f"Using multipart upload with {parts} parts")
            job_response = self._multipart_upload(project_id, csv_file_path, parts, dataset_name)
        
        # Poll for job completion if requested
        if poll_job:
            success = self.poll_job_status(job_response.id, poll_interval)
            if not success:
                raise Exception(f"Job {job_response.id} failed")
        
        return job_response
    
    def _single_part_upload(self, project_id: str, csv_file_path: str, dataset_name: str):
        """
        Handle single-part upload for smaller files.
        
        Args:
            project_id: Project ID
            csv_file_path: Path to CSV file
            dataset_name: Dataset name
        
        Returns:
            Job response
        """
        from cm_python_openapi_sdk.models.data_pull_job_request import DataPullJobRequest
        from cm_python_openapi_sdk.models.data_pull_request import DataPullRequest
        from cm_python_openapi_sdk.models.general_job_request import GeneralJobRequest
        from cm_python_openapi_sdk.models.data_pull_request_csv_options import DataPullRequestCsvOptions
        
        # Initialize upload
        logger.debug(f"Initializing upload for project {project_id}")
        upload_response = self.data_upload_api.data_upload(project_id=project_id)
        logger.debug(f"Upload response received")
        
        # Get the upload URL
        upload_url = upload_response.actual_instance.upload_url_encoded
        logger.debug(f"Got upload URL")
        
        # Upload the file
        self._upload_file(upload_url, csv_file_path)
        
        # Create and submit data pull job
        data_pull_request = DataPullRequest(
            dataset=dataset_name,
            mode="full",
            type="csv",
            upload=upload_response.actual_instance.links[1]["href"],
            csvOptions=DataPullRequestCsvOptions()
        )
        
        job_request = DataPullJobRequest(
            type="dataPull",
            projectId=project_id,
            content=data_pull_request
        )
        
        submit_request = GeneralJobRequest(actual_instance=job_request)
        job_response = self.jobs_api.submit_job_execution(submit_request)
        logger.debug(f"Job submitted with ID: {job_response.id}")
        
        return job_response
    
    def _multipart_upload(
        self, 
        project_id: str, 
        csv_file_path: str, 
        parts: int,
        dataset_name: str
    ):
        """
        Handle multipart upload for larger files.
        
        Args:
            project_id: Project ID
            csv_file_path: Path to CSV file
            parts: Number of parts to split into
            dataset_name: Dataset name
        
        Returns:
            Job response
        """
        from cm_python_openapi_sdk.models.data_pull_job_request import DataPullJobRequest
        from cm_python_openapi_sdk.models.data_pull_request import DataPullRequest
        from cm_python_openapi_sdk.models.general_job_request import GeneralJobRequest
        from cm_python_openapi_sdk.models.data_pull_request_csv_options import DataPullRequestCsvOptions
        from cm_python_openapi_sdk.models.data_complete_multipart_upload_request import DataCompleteMultipartUploadRequest
        from utils.csv_file_splitter import CSVFileSplitter
        
        # Initialize multipart upload
        upload_response = self.data_upload_api.data_upload(project_id=project_id, parts=parts)
        
        # Get the upload URLs
        upload_urls = upload_response.actual_instance.upload_urls_encoded
        
        uploaded_parts = []
        
        # Use CSVFileSplitter to split and upload
        file_splitter = CSVFileSplitter(self.chunk_size)
        with file_splitter as splitter:
            for temp_file_path, part_number in splitter.split_file(csv_file_path, parts):
                try:
                    logger.debug(f"Uploading part {part_number}/{parts}")
                    etag = self._upload_part(upload_urls[part_number - 1], temp_file_path)
                    uploaded_parts.append({
                        "eTag": etag,
                        "partNumber": part_number
                    })
                except Exception as e:
                    logger.error(f"Failed to upload part {part_number}: {e}")
                    raise
        
        # Complete the multipart upload
        complete_request = DataCompleteMultipartUploadRequest(
            id=upload_response.actual_instance.id,
            uploadId=upload_response.actual_instance.upload_id,
            partETags=uploaded_parts
        )
        
        complete_response = self.data_upload_api.complete_multipart_upload(
            project_id=project_id,
            id=upload_response.actual_instance.id,
            data_complete_multipart_upload_request=complete_request
        )
        
        # Create and submit data pull job
        data_pull_request = DataPullRequest(
            dataset=dataset_name,
            mode="full",
            type="csv",
            upload=upload_response.actual_instance.links[1]["href"],
            csvOptions=DataPullRequestCsvOptions()
        )
        
        job_request = DataPullJobRequest(
            type="dataPull",
            projectId=project_id,
            content=data_pull_request
        )
        
        submit_request = GeneralJobRequest(actual_instance=job_request)
        job_response = self.jobs_api.submit_job_execution(submit_request)
        logger.debug(f"Job submitted with ID: {job_response.id}")
        
        return job_response
    
    def _upload_file(self, url: str, csv_file_path: str) -> None:
        """
        Upload a file to a presigned URL.
        
        Args:
            url: Presigned URL
            csv_file_path: Path to the file to upload
        
        Raises:
            requests.exceptions.RequestException: If upload fails
        """
        logger.debug(f"Uploading file to presigned URL")
        
        try:
            with open(csv_file_path, 'rb') as f:
                file_size = os.path.getsize(csv_file_path)
                logger.debug(f"File size: {file_size} bytes")
                
                headers = {
                    'Content-Type': self.content_type,
                    'Content-Length': str(file_size)
                }
                
                response = requests.put(url, data=f, headers=headers)
                
                if response.status_code != 200:
                    logger.error(f"Upload failed with status {response.status_code}")
                    logger.error(f"Response content: {response.text}")
                
                response.raise_for_status()
                
        except Exception as e:
            logger.error(f"Error during file upload: {str(e)}")
            raise
    
    def _upload_part(self, url: str, file_path: str) -> str:
        """
        Upload a GZIP compressed part to presigned URL.
        
        Args:
            url: Presigned URL
            file_path: Path to the file to upload
        
        Returns:
            ETag from the response
        
        Raises:
            requests.exceptions.RequestException: If upload fails
        """
        logger.debug(f"Uploading GZIP compressed part")
        
        try:
            # Read and compress the file content
            with open(file_path, 'rb') as f:
                file_content = f.read()
            
            compressed_content = gzip.compress(file_content)
            compressed_size = len(compressed_content)
            logger.debug(
                f"Original size: {len(file_content)} bytes, "
                f"Compressed size: {compressed_size} bytes"
            )
            
            headers = {
                'Content-Type': self.content_type,
                'Content-Length': str(compressed_size)
            }
            
            response = requests.put(url, data=compressed_content, headers=headers)
            
            if response.status_code != 200:
                logger.error(f"Upload failed with status {response.status_code}")
                logger.error(f"Response content: {response.text}")
            
            response.raise_for_status()
            
            # Get ETag from response
            etag = response.headers.get('ETag')
            if not etag:
                raise ValueError("No ETag received in response")
            
            return etag
            
        except Exception as e:
            logger.error(f"Error during part upload: {str(e)}")
            raise
    
    def poll_job_status(self, job_id: str, poll_interval: int = 5, timeout: Optional[int] = None) -> bool:
        """
        Poll the status of a job until it completes or fails.
        
        Args:
            job_id: The ID of the job to poll
            poll_interval: Seconds between status checks
            timeout: Maximum seconds to wait (None for no timeout)
        
        Returns:
            True if job succeeded, False if it failed
        
        Raises:
            TimeoutError: If timeout is reached
        """
        start_time = time.time()
        
        while True:
            try:
                job_status = self.jobs_api.get_job_status(job_id, "dataPull")
                logger.debug(f"Job status: {job_status.status}")
                
                if job_status.status == "SUCCEEDED":
                    logger.info("Job completed successfully")
                    return True
                elif job_status.status == "FAILED":
                    logger.error(f"Job failed: {job_status.message}")
                    return False
                
                # Check timeout
                if timeout and (time.time() - start_time) > timeout:
                    raise TimeoutError(f"Job {job_id} did not complete within {timeout} seconds")
                
                time.sleep(poll_interval)
                
            except Exception as e:
                logger.error(f"Error polling job status: {str(e)}")
                raise
    
    def get_job_status(self, job_id: str):
        """
        Get the current status of a data pull job.
        
        Args:
            job_id: The ID of the job
        
        Returns:
            Job status response
        """
        return self.jobs_api.get_job_status(job_id, type="dataPull")
