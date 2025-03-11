# MapContextMenuDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MapContextMenuItemAbstractType]**](MapContextMenuItemAbstractType.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.map_context_menu_dto import MapContextMenuDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MapContextMenuDTO from a JSON string
map_context_menu_dto_instance = MapContextMenuDTO.from_json(json)
# print the JSON string representation of the object
print(MapContextMenuDTO.to_json())

# convert the object into a dict
map_context_menu_dto_dict = map_context_menu_dto_instance.to_dict()
# create an instance of MapContextMenuDTO from a dict
map_context_menu_dto_from_dict = MapContextMenuDTO.from_dict(map_context_menu_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


