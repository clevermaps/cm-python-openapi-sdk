# MapContentDTOOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center** | [**CenterDTO**](CenterDTO.md) |  | [optional] 
**zoom** | **int** |  | [optional] 
**min_zoom** | **int** |  | [optional] 
**max_zoom** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.map_content_dto_options import MapContentDTOOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MapContentDTOOptions from a JSON string
map_content_dto_options_instance = MapContentDTOOptions.from_json(json)
# print the JSON string representation of the object
print(MapContentDTOOptions.to_json())

# convert the object into a dict
map_content_dto_options_dict = map_content_dto_options_instance.to_dict()
# create an instance of MapContentDTOOptions from a dict
map_content_dto_options_from_dict = MapContentDTOOptions.from_dict(map_content_dto_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


