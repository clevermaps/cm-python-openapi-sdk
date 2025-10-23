# clients/data_dump_client.py
import time
import os
import logging
from typing import Optional

import requests

from . import BaseClient

logger = logging.getLogger(__name__)


class DataDumpClient(BaseClient):
    def dump_dataset_to_csv(
        self, 
        project_id: str, 
        dataset: str, 
        output_path: str,
        poll_interval: int = 5
    ) -> str:
        """
        Dump a dataset to a CSV file.
        
        This method handles the complete workflow:
        1. Submits a data dump job
        2. Polls for job completion
        3. Downloads the resulting CSV file
        
        Args:
            project_id: The ID of the project containing the dataset
            dataset: The name of the dataset to dump
            output_path: Directory path where to save the CSV file
            poll_interval: Seconds between status checks (default: 5)
        
        Returns:
            Path to the downloaded CSV file
        
        Raises:
            Exception: If the job fails or the download fails
        """
        logger.debug(f"Starting data dump for project {project_id}, dataset {dataset}")
        
        # Import models here to avoid circular dependencies
        from cm_python_openapi_sdk.models.data_dump_job_request import DataDumpJobRequest
        from cm_python_openapi_sdk.models.data_dump_request import DataDumpRequest
        from cm_python_openapi_sdk.models.general_job_request import GeneralJobRequest
        
        # Create an output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        logger.debug(f"Ensured output directory exists: {output_path}")
        
        # Prepare the job request
        data_dump_request = DataDumpRequest(
            dataset=dataset
        )
        
        job_request = DataDumpJobRequest(
            type="dataDump",
            projectId=project_id,
            content=data_dump_request
        )
        
        submit_request = GeneralJobRequest(actual_instance=job_request)
        
        # Submit the job
        logger.debug("Submitting data dump job")
        job_response = self.jobs_api.submit_job_execution(submit_request)
        job_id = job_response.id
        logger.debug(f"Job submitted with ID: {job_id}")
        
        # Poll for job completion
        logger.debug("Polling for job completion")
        self._wait_for_job_completion(job_id, poll_interval)
        
        # Get the result file URL and download
        job_status = self.jobs_api.get_job_status(job_id, type="dataDump")
        result_url = job_status.result.get("links")[0].get("href")
        
        if not result_url:
            error_msg = "No result file URL found in job response"
            logger.error(error_msg)
            raise Exception(error_msg)
        
        logger.debug(f"Got result file URL: {result_url}")
        
        # Download the file
        local_filename = os.path.join(output_path, f"{dataset}.csv")
        self._download_file(result_url, local_filename)
        
        logger.debug(f"File downloaded successfully: {local_filename}")
        return local_filename
    
    def _wait_for_job_completion(
        self, 
        job_id: str, 
        poll_interval: int = 5,
        timeout: Optional[int] = None
    ) -> None:
        """
        Poll for job completion until it succeeds or fails.
        
        Args:
            job_id: The ID of the job to monitor
            poll_interval: Seconds between status checks
            timeout: Maximum seconds to wait (None for no timeout)
        
        Raises:
            Exception: If the job fails
            TimeoutError: If timeout is reached
        """
        start_time = time.time()
        
        while True:
            job_status = self.jobs_api.get_job_status(job_id, type="dataDump")
            logger.debug(f"Current job status: {job_status.status}")
            
            if job_status.status == "SUCCEEDED":
                logger.debug("Job completed successfully")
                return
            elif job_status.status == "FAILED":
                error_msg = f"Job failed: {job_status.error}"
                logger.error(error_msg)
                raise Exception(error_msg)
            
            # Check timeout
            if timeout and (time.time() - start_time) > timeout:
                raise TimeoutError(f"Job {job_id} did not complete within {timeout} seconds")
            
            time.sleep(poll_interval)
    
    def _download_file(self, result_url: str, local_filename: str) -> None:
        """
        Download a file from the API.
        
        Args:
            result_url: Relative URL path to the file
            local_filename: Local path where to save the file
        
        Raises:
            Exception: If the download fails
        """
        logger.debug(f"Downloading file to: {local_filename}")
        
        # Get the full URL by combining the base URL with the relative path
        # Avoid duplicating /rest if result_url already contains it
        full_url = self.api_client.configuration.host + result_url[5:]  # Remove /rest from result_url
        logger.debug(f"Full URL: {full_url}")
        
        try:
            # Get the authorization header from the API client configuration
            headers = {
                'Authorization': f"Bearer {self.api_client.configuration.access_token}"
            }
            response = requests.get(full_url, headers=headers)
            response.raise_for_status()
            
            with open(local_filename, 'wb') as f:
                f.write(response.content)
            
            logger.debug(f"File downloaded successfully: {local_filename}")
            
        except Exception as e:
            error_msg = f"Failed to download file: {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)
    
    def get_job_status(self, job_id: str):
        """
        Get the current status of a data dump job.
        
        Args:
            job_id: The ID of the job
        
        Returns:
            Job status response
        """
        return self.jobs_api.get_job_status(job_id, type="dataDump")
