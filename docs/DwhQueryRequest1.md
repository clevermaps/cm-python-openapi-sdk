# DwhQueryRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_context** | **object** |  | [optional] 
**properties** | [**List[DwhQueryPropertyTypes]**](DwhQueryPropertyTypes.md) |  | 
**filter_by** | [**List[FilterBy]**](FilterBy.md) |  | [optional] 
**having** | [**List[Having1]**](Having1.md) |  | [optional] 
**result_set_filter** | [**List[ResultSetFilter]**](ResultSetFilter.md) |  | [optional] 
**order_by** | [**List[OrderBy]**](OrderBy.md) |  | [optional] 
**variables** | [**List[VariableValue]**](VariableValue.md) |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_request1 import DwhQueryRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryRequest1 from a JSON string
dwh_query_request1_instance = DwhQueryRequest1.from_json(json)
# print the JSON string representation of the object
print(DwhQueryRequest1.to_json())

# convert the object into a dict
dwh_query_request1_dict = dwh_query_request1_instance.to_dict()
# create an instance of DwhQueryRequest1 from a dict
dwh_query_request1_from_dict = DwhQueryRequest1.from_dict(dwh_query_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


