# MapContentDTOBaseLayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**menu** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.map_content_dto_base_layer import MapContentDTOBaseLayer

# TODO update the JSON string below
json = "{}"
# create an instance of MapContentDTOBaseLayer from a JSON string
map_content_dto_base_layer_instance = MapContentDTOBaseLayer.from_json(json)
# print the JSON string representation of the object
print(MapContentDTOBaseLayer.to_json())

# convert the object into a dict
map_content_dto_base_layer_dict = map_content_dto_base_layer_instance.to_dict()
# create an instance of MapContentDTOBaseLayer from a dict
map_content_dto_base_layer_from_dict = MapContentDTOBaseLayer.from_dict(map_content_dto_base_layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


