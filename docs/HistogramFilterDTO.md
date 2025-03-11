# HistogramFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**var_property** | **str** |  | 
**format** | [**FormatDTO**](FormatDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.histogram_filter_dto import HistogramFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HistogramFilterDTO from a JSON string
histogram_filter_dto_instance = HistogramFilterDTO.from_json(json)
# print the JSON string representation of the object
print(HistogramFilterDTO.to_json())

# convert the object into a dict
histogram_filter_dto_dict = histogram_filter_dto_instance.to_dict()
# create an instance of HistogramFilterDTO from a dict
histogram_filter_dto_from_dict = HistogramFilterDTO.from_dict(histogram_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


