# MarkerSelectorPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[MarkerSelectorResponseDTO]**](MarkerSelectorResponseDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.marker_selector_paged_model_dto import MarkerSelectorPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerSelectorPagedModelDTO from a JSON string
marker_selector_paged_model_dto_instance = MarkerSelectorPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerSelectorPagedModelDTO.to_json())

# convert the object into a dict
marker_selector_paged_model_dto_dict = marker_selector_paged_model_dto_instance.to_dict()
# create an instance of MarkerSelectorPagedModelDTO from a dict
marker_selector_paged_model_dto_from_dict = MarkerSelectorPagedModelDTO.from_dict(marker_selector_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


