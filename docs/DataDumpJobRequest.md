# DataDumpJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**DataDumpRequest**](DataDumpRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_dump_job_request import DataDumpJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataDumpJobRequest from a JSON string
data_dump_job_request_instance = DataDumpJobRequest.from_json(json)
# print the JSON string representation of the object
print(DataDumpJobRequest.to_json())

# convert the object into a dict
data_dump_job_request_dict = data_dump_job_request_instance.to_dict()
# create an instance of DataDumpJobRequest from a dict
data_dump_job_request_from_dict = DataDumpJobRequest.from_dict(data_dump_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


