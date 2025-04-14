# HighlightDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.highlight_dto import HighlightDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HighlightDTO from a JSON string
highlight_dto_instance = HighlightDTO.from_json(json)
# print the JSON string representation of the object
print(HighlightDTO.to_json())

# convert the object into a dict
highlight_dto_dict = highlight_dto_instance.to_dict()
# create an instance of HighlightDTO from a dict
highlight_dto_from_dict = HighlightDTO.from_dict(highlight_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


