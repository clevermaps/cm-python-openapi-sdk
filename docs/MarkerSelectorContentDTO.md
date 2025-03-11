# MarkerSelectorContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CategoryDTO]**](CategoryDTO.md) |  | [optional] 
**granularity_categories** | [**List[GranularityCategoryDTO]**](GranularityCategoryDTO.md) |  | [optional] 
**hide_granularity** | **bool** |  | [optional] 
**keep_filtered** | [**MarkerSelectorContentDTOKeepFiltered**](MarkerSelectorContentDTOKeepFiltered.md) |  | [optional] 
**show_indicator_values_on_map** | **bool** |  | [optional] 
**cluster_markers** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.marker_selector_content_dto import MarkerSelectorContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerSelectorContentDTO from a JSON string
marker_selector_content_dto_instance = MarkerSelectorContentDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerSelectorContentDTO.to_json())

# convert the object into a dict
marker_selector_content_dto_dict = marker_selector_content_dto_instance.to_dict()
# create an instance of MarkerSelectorContentDTO from a dict
marker_selector_content_dto_from_dict = MarkerSelectorContentDTO.from_dict(marker_selector_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


