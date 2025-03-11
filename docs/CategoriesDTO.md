# CategoriesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**split_property** | **str** |  | [optional] 
**attribute_style** | **str** |  | [optional] 
**indicator** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**visualized** | **bool** |  | [optional] 
**filterable** | **bool** |  | [optional] 
**hide_null_items** | **bool** |  | [optional] 
**size_limit** | **int** |  | [optional] 
**order_by** | [**OrderByDTO**](OrderByDTO.md) |  | [optional] 
**vertical** | **bool** |  | [optional] 
**condensed** | **bool** |  | [optional] 
**dual_property** | **str** |  | [optional] 
**dual_attribute_style** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.categories_dto import CategoriesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesDTO from a JSON string
categories_dto_instance = CategoriesDTO.from_json(json)
# print the JSON string representation of the object
print(CategoriesDTO.to_json())

# convert the object into a dict
categories_dto_dict = categories_dto_instance.to_dict()
# create an instance of CategoriesDTO from a dict
categories_dto_from_dict = CategoriesDTO.from_dict(categories_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


