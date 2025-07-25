# AttributeStyleResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**AttributeStyleContentDTO**](AttributeStyleContentDTO.md) |  | 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 
**access_info** | [**AccessInfoDTO**](AccessInfoDTO.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.attribute_style_response_dto import AttributeStyleResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeStyleResponseDTO from a JSON string
attribute_style_response_dto_instance = AttributeStyleResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeStyleResponseDTO.to_json())

# convert the object into a dict
attribute_style_response_dto_dict = attribute_style_response_dto_instance.to_dict()
# create an instance of AttributeStyleResponseDTO from a dict
attribute_style_response_dto_from_dict = AttributeStyleResponseDTO.from_dict(attribute_style_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


