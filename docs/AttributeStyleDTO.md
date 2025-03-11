# AttributeStyleDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**AttributeStyleContentDTO**](AttributeStyleContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.attribute_style_dto import AttributeStyleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeStyleDTO from a JSON string
attribute_style_dto_instance = AttributeStyleDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeStyleDTO.to_json())

# convert the object into a dict
attribute_style_dto_dict = attribute_style_dto_instance.to_dict()
# create an instance of AttributeStyleDTO from a dict
attribute_style_dto_from_dict = AttributeStyleDTO.from_dict(attribute_style_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


