# ExportJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**ExportRequest**](ExportRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.export_job_request import ExportJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportJobRequest from a JSON string
export_job_request_instance = ExportJobRequest.from_json(json)
# print the JSON string representation of the object
print(ExportJobRequest.to_json())

# convert the object into a dict
export_job_request_dict = export_job_request_instance.to_dict()
# create an instance of ExportJobRequest from a dict
export_job_request_from_dict = ExportJobRequest.from_dict(export_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


