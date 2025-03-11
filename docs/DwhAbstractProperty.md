# DwhAbstractProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**column** | **str** |  | 
**type** | **str** |  | 
**filterable** | **bool** |  | [optional] [default to True]
**calculated** | **bool** |  | [optional] 
**display_options** | [**DisplayOptionsDTO**](DisplayOptionsDTO.md) |  | [optional] 
**geometry** | **object** |  | 
**foreign_key** | **object** |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_abstract_property import DwhAbstractProperty

# TODO update the JSON string below
json = "{}"
# create an instance of DwhAbstractProperty from a JSON string
dwh_abstract_property_instance = DwhAbstractProperty.from_json(json)
# print the JSON string representation of the object
print(DwhAbstractProperty.to_json())

# convert the object into a dict
dwh_abstract_property_dict = dwh_abstract_property_instance.to_dict()
# create an instance of DwhAbstractProperty from a dict
dwh_abstract_property_from_dict = DwhAbstractProperty.from_dict(dwh_abstract_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


