# MarkerPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[MarkerResponseDTO]**](MarkerResponseDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.marker_paged_model_dto import MarkerPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerPagedModelDTO from a JSON string
marker_paged_model_dto_instance = MarkerPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerPagedModelDTO.to_json())

# convert the object into a dict
marker_paged_model_dto_dict = marker_paged_model_dto_instance.to_dict()
# create an instance of MarkerPagedModelDTO from a dict
marker_paged_model_dto_from_dict = MarkerPagedModelDTO.from_dict(marker_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


