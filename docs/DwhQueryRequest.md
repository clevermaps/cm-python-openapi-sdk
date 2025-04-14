# DwhQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_context** | **object** |  | [optional] 
**properties** | [**List[DwhQueryPropertyTypes]**](DwhQueryPropertyTypes.md) |  | 
**filter_by** | [**List[FilterBy]**](FilterBy.md) |  | [optional] 
**having** | [**List[Having]**](Having.md) |  | [optional] 
**result_set_filter** | [**List[ResultSetFilter]**](ResultSetFilter.md) |  | [optional] 
**order_by** | [**List[OrderBy]**](OrderBy.md) |  | [optional] 
**variables** | [**List[VariableValue]**](VariableValue.md) |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_request import DwhQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryRequest from a JSON string
dwh_query_request_instance = DwhQueryRequest.from_json(json)
# print the JSON string representation of the object
print(DwhQueryRequest.to_json())

# convert the object into a dict
dwh_query_request_dict = dwh_query_request_instance.to_dict()
# create an instance of DwhQueryRequest from a dict
dwh_query_request_from_dict = DwhQueryRequest.from_dict(dwh_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


