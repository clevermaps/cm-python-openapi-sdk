# DataPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | 
**mode** | **str** |  | 
**type** | **str** |  | 
**upload** | **str** |  | [optional] 
**s3_upload** | [**DataPullRequestS3Upload**](DataPullRequestS3Upload.md) |  | [optional] 
**https_upload** | [**DataPullRequestHttpsUpload**](DataPullRequestHttpsUpload.md) |  | [optional] 
**csv_options** | [**DataPullRequestCsvOptions**](DataPullRequestCsvOptions.md) |  | [optional] 
**skip_refreshing_materialized_views** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_pull_request import DataPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataPullRequest from a JSON string
data_pull_request_instance = DataPullRequest.from_json(json)
# print the JSON string representation of the object
print(DataPullRequest.to_json())

# convert the object into a dict
data_pull_request_dict = data_pull_request_instance.to_dict()
# create an instance of DataPullRequest from a dict
data_pull_request_from_dict = DataPullRequest.from_dict(data_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


