# MarkerContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**style** | **str** |  | 
**property_filters** | [**List[MarkerContentDTOPropertyFiltersInner]**](MarkerContentDTOPropertyFiltersInner.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.marker_content_dto import MarkerContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerContentDTO from a JSON string
marker_content_dto_instance = MarkerContentDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerContentDTO.to_json())

# convert the object into a dict
marker_content_dto_dict = marker_content_dto_instance.to_dict()
# create an instance of MarkerContentDTO from a dict
marker_content_dto_from_dict = MarkerContentDTO.from_dict(marker_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


