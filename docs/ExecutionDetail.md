# ExecutionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**double_counting_warnings** | [**List[DoubleCountingWarnings]**](DoubleCountingWarnings.md) |  | [optional] 
**dwh_query_metric_names** | **List[str]** |  | [optional] 
**feature** | **str** |  | [optional] 
**view_name** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.execution_detail import ExecutionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDetail from a JSON string
execution_detail_instance = ExecutionDetail.from_json(json)
# print the JSON string representation of the object
print(ExecutionDetail.to_json())

# convert the object into a dict
execution_detail_dict = execution_detail_instance.to_dict()
# create an instance of ExecutionDetail from a dict
execution_detail_from_dict = ExecutionDetail.from_dict(execution_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


