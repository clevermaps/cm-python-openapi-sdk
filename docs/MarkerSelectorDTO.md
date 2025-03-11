# MarkerSelectorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**MarkerSelectorContentDTO**](MarkerSelectorContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.marker_selector_dto import MarkerSelectorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerSelectorDTO from a JSON string
marker_selector_dto_instance = MarkerSelectorDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerSelectorDTO.to_json())

# convert the object into a dict
marker_selector_dto_dict = marker_selector_dto_instance.to_dict()
# create an instance of MarkerSelectorDTO from a dict
marker_selector_dto_from_dict = MarkerSelectorDTO.from_dict(marker_selector_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


