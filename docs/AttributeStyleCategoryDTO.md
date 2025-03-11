# AttributeStyleCategoryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**style** | [**StyleDTO**](StyleDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.attribute_style_category_dto import AttributeStyleCategoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeStyleCategoryDTO from a JSON string
attribute_style_category_dto_instance = AttributeStyleCategoryDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeStyleCategoryDTO.to_json())

# convert the object into a dict
attribute_style_category_dto_dict = attribute_style_category_dto_instance.to_dict()
# create an instance of AttributeStyleCategoryDTO from a dict
attribute_style_category_dto_from_dict = AttributeStyleCategoryDTO.from_dict(attribute_style_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


