# DwhDateRangeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | [**DateFilterDefaultValueType**](DateFilterDefaultValueType.md) |  | [optional] 
**end_date** | [**DateFilterDefaultValueType**](DateFilterDefaultValueType.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_date_range_filter import DwhDateRangeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DwhDateRangeFilter from a JSON string
dwh_date_range_filter_instance = DwhDateRangeFilter.from_json(json)
# print the JSON string representation of the object
print(DwhDateRangeFilter.to_json())

# convert the object into a dict
dwh_date_range_filter_dict = dwh_date_range_filter_instance.to_dict()
# create an instance of DwhDateRangeFilter from a dict
dwh_date_range_filter_from_dict = DwhDateRangeFilter.from_dict(dwh_date_range_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


