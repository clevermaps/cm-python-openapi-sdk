# DwhQueryNumberType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_number_type import DwhQueryNumberType

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryNumberType from a JSON string
dwh_query_number_type_instance = DwhQueryNumberType.from_json(json)
# print the JSON string representation of the object
print(DwhQueryNumberType.to_json())

# convert the object into a dict
dwh_query_number_type_dict = dwh_query_number_type_instance.to_dict()
# create an instance of DwhQueryNumberType from a dict
dwh_query_number_type_from_dict = DwhQueryNumberType.from_dict(dwh_query_number_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


