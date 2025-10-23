from cm_python_highlevel_clients.load_data_client import LoadDataClient


def test_single_part_upload(csv_path: str, project_id: str, access_token: str):
    """
    Test single-part CSV upload (for files <= 50MB)

    Args:
        csv_path (str): Path to the CSV file
        project_id (str): CleverMaps project ID
        config: Configured API client configuration
    """

    load_data_client = LoadDataClient(access_token)

    response = load_data_client.upload_data(
        project_id=project_id,
        csv_file_path=csv_path,
        dataset_name="stores"
    )

    print(f"Single-part upload completed:")
    print(f"Job ID: {response.id}")
    print(f"Job Status: {response.status}")

    success = load_data_client.poll_job_status(response.id, poll_interval=5)

    if success:
        print(f"Job {response.id} completed successfully")
    else:
        print(f"Job {response.id} failed")


def test_multipart_upload(csv_path: str, project_id: str, access_token: str):
    """
    Test multipart CSV upload (for files > 50MB)

    Args:
        csv_path (str): Path to the CSV file
        project_id (str): CleverMaps project ID
        config: Configured API client configuration
    """
    load_data_client = LoadDataClient(access_token)

    response = load_data_client.upload_data(
        project_id=project_id,
        csv_file_path=csv_path,
        dataset_name="zsj_d_dwh"
    )

    print(f"Multipart upload completed:")
    print(f"Job ID: {response.id}")
    print(f"Job Status: {response.status}")

    success = load_data_client.poll_job_status(response.id, poll_interval=5)

    if success:
        print(f"Job {response.id} completed successfully")
    else:
        print(f"Job {response.id} failed")


if __name__ == "__main__":
    PROJECT_ID = ""  # Replace with your CleverMaps project ID
    ACCESS_TOKEN = ""
    DATASET = ""  # Replace with your dataset name
    CSV_PATH = ""  # Replace with your desired output path
    CSV_PATH_MULTIPART = ""
    # Test single-part upload
    print("\nTesting single-part upload:")
    test_single_part_upload(CSV_PATH, PROJECT_ID, ACCESS_TOKEN)

    # Test multipart upload
    print("\nTesting multipart upload:")
    test_multipart_upload(CSV_PATH_MULTIPART, PROJECT_ID, ACCESS_TOKEN)