# IsochroneDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**profile** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**geometry** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.isochrone_dto import IsochroneDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IsochroneDTO from a JSON string
isochrone_dto_instance = IsochroneDTO.from_json(json)
# print the JSON string representation of the object
print(IsochroneDTO.to_json())

# convert the object into a dict
isochrone_dto_dict = isochrone_dto_instance.to_dict()
# create an instance of IsochroneDTO from a dict
isochrone_dto_from_dict = IsochroneDTO.from_dict(isochrone_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


