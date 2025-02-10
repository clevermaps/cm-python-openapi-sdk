# StyleDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fill_color** | **str** |  | [optional] 
**fill_hex_color** | **str** |  | [optional] 
**fill_opacity** | **float** |  | [optional] 
**outline_color** | **str** |  | [optional] 
**outline_hex_color** | **str** |  | [optional] 
**outline_opacity** | **float** |  | [optional] 
**outline_width** | **float** |  | [optional] 
**size** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.style_dto import StyleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of StyleDTO from a JSON string
style_dto_instance = StyleDTO.from_json(json)
# print the JSON string representation of the object
print(StyleDTO.to_json())

# convert the object into a dict
style_dto_dict = style_dto_instance.to_dict()
# create an instance of StyleDTO from a dict
style_dto_from_dict = StyleDTO.from_dict(style_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


