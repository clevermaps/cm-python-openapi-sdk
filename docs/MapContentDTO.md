# MapContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**MapContentDTOOptions**](MapContentDTOOptions.md) |  | [optional] 
**base_layer** | [**MapContentDTOBaseLayer**](MapContentDTOBaseLayer.md) |  | [optional] 
**context_menu** | [**MapContextMenuDTO**](MapContextMenuDTO.md) |  | [optional] 
**layers** | [**List[LayerDTO]**](LayerDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.map_content_dto import MapContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MapContentDTO from a JSON string
map_content_dto_instance = MapContentDTO.from_json(json)
# print the JSON string representation of the object
print(MapContentDTO.to_json())

# convert the object into a dict
map_content_dto_dict = map_content_dto_instance.to_dict()
# create an instance of MapContentDTO from a dict
map_content_dto_from_dict = MapContentDTO.from_dict(map_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


