# CsvHeaderOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_dwh_property_id** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.csv_header_override import CsvHeaderOverride

# TODO update the JSON string below
json = "{}"
# create an instance of CsvHeaderOverride from a JSON string
csv_header_override_instance = CsvHeaderOverride.from_json(json)
# print the JSON string representation of the object
print(CsvHeaderOverride.to_json())

# convert the object into a dict
csv_header_override_dict = csv_header_override_instance.to_dict()
# create an instance of CsvHeaderOverride from a dict
csv_header_override_from_dict = CsvHeaderOverride.from_dict(csv_header_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


