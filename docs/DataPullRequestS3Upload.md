# DataPullRequestS3Upload

Object specifying properties for dataPull from any AWS S3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | AWS S3 URI (e.g. s3://can-s3-dwh-pull-test/shops.csv). | 
**access_key_id** | **str** | AWS S3 Access Key ID with access to the file specified in &#39;uri&#39;. | [optional] 
**secret_access_key** | **str** | AWS S3 Secret Access Key with access to the file specified in &#39;uri&#39;. | [optional] 
**region** | **str** | AWS S3 region of the file. | [optional] 
**endpoint_override** | **str** | AWS S3 region of the file. | [optional] 
**force_path_style** | **bool** | If true, path style is forced for S3 URIs, otherwise virtual hosted style is used. | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_pull_request_s3_upload import DataPullRequestS3Upload

# TODO update the JSON string below
json = "{}"
# create an instance of DataPullRequestS3Upload from a JSON string
data_pull_request_s3_upload_instance = DataPullRequestS3Upload.from_json(json)
# print the JSON string representation of the object
print(DataPullRequestS3Upload.to_json())

# convert the object into a dict
data_pull_request_s3_upload_dict = data_pull_request_s3_upload_instance.to_dict()
# create an instance of DataPullRequestS3Upload from a dict
data_pull_request_s3_upload_from_dict = DataPullRequestS3Upload.from_dict(data_pull_request_s3_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


