# DwhQueryVariableType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_variable_type import DwhQueryVariableType

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryVariableType from a JSON string
dwh_query_variable_type_instance = DwhQueryVariableType.from_json(json)
# print the JSON string representation of the object
print(DwhQueryVariableType.to_json())

# convert the object into a dict
dwh_query_variable_type_dict = dwh_query_variable_type_instance.to_dict()
# create an instance of DwhQueryVariableType from a dict
dwh_query_variable_type_from_dict = DwhQueryVariableType.from_dict(dwh_query_variable_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


