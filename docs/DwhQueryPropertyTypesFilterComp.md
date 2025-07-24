# DwhQueryPropertyTypesFilterComp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | 
**metric** | **str** |  | 
**content** | **List[object]** |  | 
**options** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_property_types_filter_comp import DwhQueryPropertyTypesFilterComp

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryPropertyTypesFilterComp from a JSON string
dwh_query_property_types_filter_comp_instance = DwhQueryPropertyTypesFilterComp.from_json(json)
# print the JSON string representation of the object
print(DwhQueryPropertyTypesFilterComp.to_json())

# convert the object into a dict
dwh_query_property_types_filter_comp_dict = dwh_query_property_types_filter_comp_instance.to_dict()
# create an instance of DwhQueryPropertyTypesFilterComp from a dict
dwh_query_property_types_filter_comp_from_dict = DwhQueryPropertyTypesFilterComp.from_dict(dwh_query_property_types_filter_comp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


