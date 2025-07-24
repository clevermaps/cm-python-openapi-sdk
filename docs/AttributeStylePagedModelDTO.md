# AttributeStylePagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[AttributeStyleResponseDTO]**](AttributeStyleResponseDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.attribute_style_paged_model_dto import AttributeStylePagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeStylePagedModelDTO from a JSON string
attribute_style_paged_model_dto_instance = AttributeStylePagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeStylePagedModelDTO.to_json())

# convert the object into a dict
attribute_style_paged_model_dto_dict = attribute_style_paged_model_dto_instance.to_dict()
# create an instance of AttributeStylePagedModelDTO from a dict
attribute_style_paged_model_dto_from_dict = AttributeStylePagedModelDTO.from_dict(attribute_style_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


