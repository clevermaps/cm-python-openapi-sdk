# MarkerContentDTOPropertyFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | 
**value** | **List[object]** |  | 
**operator** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.marker_content_dto_property_filters_inner import MarkerContentDTOPropertyFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerContentDTOPropertyFiltersInner from a JSON string
marker_content_dto_property_filters_inner_instance = MarkerContentDTOPropertyFiltersInner.from_json(json)
# print the JSON string representation of the object
print(MarkerContentDTOPropertyFiltersInner.to_json())

# convert the object into a dict
marker_content_dto_property_filters_inner_dict = marker_content_dto_property_filters_inner_instance.to_dict()
# create an instance of MarkerContentDTOPropertyFiltersInner from a dict
marker_content_dto_property_filters_inner_from_dict = MarkerContentDTOPropertyFiltersInner.from_dict(marker_content_dto_property_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


