# TimeSeriesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**indicator** | **str** |  | [optional] 
**collapsed** | **bool** |  | [optional] 
**visualized** | **bool** |  | [optional] 
**default_period** | **str** |  | [optional] 
**additional_series** | [**List[AdditionalSeriesLinkDTO]**](AdditionalSeriesLinkDTO.md) |  | [optional] 
**annotations** | [**List[AnnotationLinkDTO]**](AnnotationLinkDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_series_dto import TimeSeriesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesDTO from a JSON string
time_series_dto_instance = TimeSeriesDTO.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesDTO.to_json())

# convert the object into a dict
time_series_dto_dict = time_series_dto_instance.to_dict()
# create an instance of TimeSeriesDTO from a dict
time_series_dto_from_dict = TimeSeriesDTO.from_dict(time_series_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


