# FlowRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 
**parameters** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.flow_run_request import FlowRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRunRequest from a JSON string
flow_run_request_instance = FlowRunRequest.from_json(json)
# print the JSON string representation of the object
print(FlowRunRequest.to_json())

# convert the object into a dict
flow_run_request_dict = flow_run_request_instance.to_dict()
# create an instance of FlowRunRequest from a dict
flow_run_request_from_dict = FlowRunRequest.from_dict(flow_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


