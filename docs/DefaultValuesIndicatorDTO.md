# DefaultValuesIndicatorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[Optional[float]]** |  | [optional] 
**breaks** | **List[float]** |  | [optional] 
**display_intervals** | **List[int]** |  | [optional] 
**granularity** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.default_values_indicator_dto import DefaultValuesIndicatorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultValuesIndicatorDTO from a JSON string
default_values_indicator_dto_instance = DefaultValuesIndicatorDTO.from_json(json)
# print the JSON string representation of the object
print(DefaultValuesIndicatorDTO.to_json())

# convert the object into a dict
default_values_indicator_dto_dict = default_values_indicator_dto_instance.to_dict()
# create an instance of DefaultValuesIndicatorDTO from a dict
default_values_indicator_dto_from_dict = DefaultValuesIndicatorDTO.from_dict(default_values_indicator_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


