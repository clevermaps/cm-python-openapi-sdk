# MapDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**MapContentDTO**](MapContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.map_dto import MapDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MapDTO from a JSON string
map_dto_instance = MapDTO.from_json(json)
# print the JSON string representation of the object
print(MapDTO.to_json())

# convert the object into a dict
map_dto_dict = map_dto_instance.to_dict()
# create an instance of MapDTO from a dict
map_dto_from_dict = MapDTO.from_dict(map_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


