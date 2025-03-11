# MapOptionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center** | [**CenterDTO**](CenterDTO.md) |  | [optional] 
**zoom** | **int** |  | [optional] 
**min_zoom** | **int** |  | [optional] 
**max_zoom** | **int** |  | [optional] 
**tile_layer_menu** | **bool** |  | [optional] 
**tile_layer** | **str** |  | [optional] 
**custom_tile_layer** | [**MapOptionsDTOCustomTileLayer**](MapOptionsDTOCustomTileLayer.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.map_options_dto import MapOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MapOptionsDTO from a JSON string
map_options_dto_instance = MapOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(MapOptionsDTO.to_json())

# convert the object into a dict
map_options_dto_dict = map_options_dto_instance.to_dict()
# create an instance of MapOptionsDTO from a dict
map_options_dto_from_dict = MapOptionsDTO.from_dict(map_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


