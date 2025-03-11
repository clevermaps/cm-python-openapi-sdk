# AttributeStyleFallbackCategoryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**style** | [**StyleDTO**](StyleDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.attribute_style_fallback_category_dto import AttributeStyleFallbackCategoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeStyleFallbackCategoryDTO from a JSON string
attribute_style_fallback_category_dto_instance = AttributeStyleFallbackCategoryDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeStyleFallbackCategoryDTO.to_json())

# convert the object into a dict
attribute_style_fallback_category_dto_dict = attribute_style_fallback_category_dto_instance.to_dict()
# create an instance of AttributeStyleFallbackCategoryDTO from a dict
attribute_style_fallback_category_dto_from_dict = AttributeStyleFallbackCategoryDTO.from_dict(attribute_style_fallback_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


