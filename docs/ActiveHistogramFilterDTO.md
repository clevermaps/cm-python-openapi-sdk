# ActiveHistogramFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_values** | [**DefaultValuesHistogramDTO**](DefaultValuesHistogramDTO.md) |  | 
**type** | **str** |  | 
**var_property** | **str** |  | 
**format** | [**FormatDTO**](FormatDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.active_histogram_filter_dto import ActiveHistogramFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveHistogramFilterDTO from a JSON string
active_histogram_filter_dto_instance = ActiveHistogramFilterDTO.from_json(json)
# print the JSON string representation of the object
print(ActiveHistogramFilterDTO.to_json())

# convert the object into a dict
active_histogram_filter_dto_dict = active_histogram_filter_dto_instance.to_dict()
# create an instance of ActiveHistogramFilterDTO from a dict
active_histogram_filter_dto_from_dict = ActiveHistogramFilterDTO.from_dict(active_histogram_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


