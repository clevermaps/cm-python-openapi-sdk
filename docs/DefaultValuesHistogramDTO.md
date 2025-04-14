# DefaultValuesHistogramDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[float]** |  | [optional] 
**null_filtered** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.default_values_histogram_dto import DefaultValuesHistogramDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultValuesHistogramDTO from a JSON string
default_values_histogram_dto_instance = DefaultValuesHistogramDTO.from_json(json)
# print the JSON string representation of the object
print(DefaultValuesHistogramDTO.to_json())

# convert the object into a dict
default_values_histogram_dto_dict = default_values_histogram_dto_instance.to_dict()
# create an instance of DefaultValuesHistogramDTO from a dict
default_values_histogram_dto_from_dict = DefaultValuesHistogramDTO.from_dict(default_values_histogram_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


