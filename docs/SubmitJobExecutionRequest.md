# SubmitJobExecutionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**ExportRequest**](ExportRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.submit_job_execution_request import SubmitJobExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitJobExecutionRequest from a JSON string
submit_job_execution_request_instance = SubmitJobExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitJobExecutionRequest.to_json())

# convert the object into a dict
submit_job_execution_request_dict = submit_job_execution_request_instance.to_dict()
# create an instance of SubmitJobExecutionRequest from a dict
submit_job_execution_request_from_dict = SubmitJobExecutionRequest.from_dict(submit_job_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


