import pytest

from cm_python_highlevel_clients import DataDumpClient

@pytest.mark.skip(reason="Integration test - run manually with actual credentials")
def test_real_dump_dataset_to_csv(project_id: str, dataset: str, output_path: str, access_token: str):
    """
    Test real data dump from CleverMaps project

    Args:
        project_id (str): CleverMaps project ID
        dataset (str): Dataset name to dump
        output_path (str): Path where to save the CSV file
        access_token (str): CleverMaps access token
    """
    sdk = DataDumpClient(api_token=access_token)

    output_file = sdk.dump_dataset_to_csv(project_id, dataset, output_path)

    print(f"Data dump completed:")
    print(f"Output file: {output_file}")

    with open(output_file, 'r') as f:
        content = f.read()
        print(f"File content length: {len(content)}")


if __name__ == "__main__":
    # # Replace these with your actual values
    # PROJECT_ID = ""  # Replace with your CleverMaps project ID
    # ACCESS_TOKEN = ""
    # DATASET = ""  # Replace with your dataset name
    # OUTPUT_PATH = ""  # Replace with your desired output path
    #
    # # Test real data dump
    # print("\nTesting real data dump:")
    # #test_real_dump_dataset_to_csv(PROJECT_ID, DATASET, OUTPUT_PATH, ACCESS_TOKEN)
    pass