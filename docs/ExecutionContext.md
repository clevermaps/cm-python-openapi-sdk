# ExecutionContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** |  | [optional] 
**view_name** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.execution_context import ExecutionContext

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionContext from a JSON string
execution_context_instance = ExecutionContext.from_json(json)
# print the JSON string representation of the object
print(ExecutionContext.to_json())

# convert the object into a dict
execution_context_dict = execution_context_instance.to_dict()
# create an instance of ExecutionContext from a dict
execution_context_from_dict = ExecutionContext.from_dict(execution_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


