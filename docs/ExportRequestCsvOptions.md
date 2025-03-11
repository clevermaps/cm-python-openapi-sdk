# ExportRequestCsvOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **bool** |  | [optional] 
**separator** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 
**escape** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.export_request_csv_options import ExportRequestCsvOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRequestCsvOptions from a JSON string
export_request_csv_options_instance = ExportRequestCsvOptions.from_json(json)
# print the JSON string representation of the object
print(ExportRequestCsvOptions.to_json())

# convert the object into a dict
export_request_csv_options_dict = export_request_csv_options_instance.to_dict()
# create an instance of ExportRequestCsvOptions from a dict
export_request_csv_options_from_dict = ExportRequestCsvOptions.from_dict(export_request_csv_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


