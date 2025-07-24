# DwhQueryPropertyTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | 
**metric** | **str** |  | 
**content** | [**List[DwhQueryPropertyTypesFunctionRowNumber]**](DwhQueryPropertyTypesFunctionRowNumber.md) |  | 
**options** | **object** |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_property_types import DwhQueryPropertyTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryPropertyTypes from a JSON string
dwh_query_property_types_instance = DwhQueryPropertyTypes.from_json(json)
# print the JSON string representation of the object
print(DwhQueryPropertyTypes.to_json())

# convert the object into a dict
dwh_query_property_types_dict = dwh_query_property_types_instance.to_dict()
# create an instance of DwhQueryPropertyTypes from a dict
dwh_query_property_types_from_dict = DwhQueryPropertyTypes.from_dict(dwh_query_property_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


