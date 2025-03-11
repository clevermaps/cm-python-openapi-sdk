# TruncateJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.truncate_job_request import TruncateJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TruncateJobRequest from a JSON string
truncate_job_request_instance = TruncateJobRequest.from_json(json)
# print the JSON string representation of the object
print(TruncateJobRequest.to_json())

# convert the object into a dict
truncate_job_request_dict = truncate_job_request_instance.to_dict()
# create an instance of TruncateJobRequest from a dict
truncate_job_request_from_dict = TruncateJobRequest.from_dict(truncate_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


