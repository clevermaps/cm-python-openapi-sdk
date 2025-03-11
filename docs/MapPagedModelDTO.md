# MapPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[MapDTO]**](MapDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.map_paged_model_dto import MapPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MapPagedModelDTO from a JSON string
map_paged_model_dto_instance = MapPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(MapPagedModelDTO.to_json())

# convert the object into a dict
map_paged_model_dto_dict = map_paged_model_dto_instance.to_dict()
# create an instance of MapPagedModelDTO from a dict
map_paged_model_dto_from_dict = MapPagedModelDTO.from_dict(map_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


