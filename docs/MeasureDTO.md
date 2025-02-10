# MeasureDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**points** | [**List[IsochroneDTO]**](IsochroneDTO.md) |  | [optional] 
**zones** | [**List[IsochroneDTO]**](IsochroneDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.measure_dto import MeasureDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureDTO from a JSON string
measure_dto_instance = MeasureDTO.from_json(json)
# print the JSON string representation of the object
print(MeasureDTO.to_json())

# convert the object into a dict
measure_dto_dict = measure_dto_instance.to_dict()
# create an instance of MeasureDTO from a dict
measure_dto_from_dict = MeasureDTO.from_dict(measure_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


