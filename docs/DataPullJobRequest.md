# DataPullJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**DataPullRequest**](DataPullRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_pull_job_request import DataPullJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataPullJobRequest from a JSON string
data_pull_job_request_instance = DataPullJobRequest.from_json(json)
# print the JSON string representation of the object
print(DataPullJobRequest.to_json())

# convert the object into a dict
data_pull_job_request_dict = data_pull_job_request_instance.to_dict()
# create an instance of DataPullJobRequest from a dict
data_pull_job_request_from_dict = DataPullJobRequest.from_dict(data_pull_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


