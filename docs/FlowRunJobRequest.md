# FlowRunJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**FlowRunRequest**](FlowRunRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.flow_run_job_request import FlowRunJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRunJobRequest from a JSON string
flow_run_job_request_instance = FlowRunJobRequest.from_json(json)
# print the JSON string representation of the object
print(FlowRunJobRequest.to_json())

# convert the object into a dict
flow_run_job_request_dict = flow_run_job_request_instance.to_dict()
# create an instance of FlowRunJobRequest from a dict
flow_run_job_request_from_dict = FlowRunJobRequest.from_dict(flow_run_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


