# DwhQueryFunctionTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | 
**metric** | **str** |  | 
**content** | [**List[DwhQueryNumberType]**](DwhQueryNumberType.md) |  | 
**options** | [**FunctionDistanceOptions**](FunctionDistanceOptions.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_function_types import DwhQueryFunctionTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryFunctionTypes from a JSON string
dwh_query_function_types_instance = DwhQueryFunctionTypes.from_json(json)
# print the JSON string representation of the object
print(DwhQueryFunctionTypes.to_json())

# convert the object into a dict
dwh_query_function_types_dict = dwh_query_function_types_instance.to_dict()
# create an instance of DwhQueryFunctionTypes from a dict
dwh_query_function_types_from_dict = DwhQueryFunctionTypes.from_dict(dwh_query_function_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


