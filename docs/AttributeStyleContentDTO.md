# AttributeStyleContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | 
**fallback_category** | [**AttributeStyleFallbackCategoryDTO**](AttributeStyleFallbackCategoryDTO.md) |  | [optional] 
**categories** | [**List[AttributeStyleCategoryDTO]**](AttributeStyleCategoryDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.attribute_style_content_dto import AttributeStyleContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeStyleContentDTO from a JSON string
attribute_style_content_dto_instance = AttributeStyleContentDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeStyleContentDTO.to_json())

# convert the object into a dict
attribute_style_content_dto_dict = attribute_style_content_dto_instance.to_dict()
# create an instance of AttributeStyleContentDTO from a dict
attribute_style_content_dto_from_dict = AttributeStyleContentDTO.from_dict(attribute_style_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


