# ValidateJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**ValidateRequest**](ValidateRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.validate_job_request import ValidateJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateJobRequest from a JSON string
validate_job_request_instance = ValidateJobRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateJobRequest.to_json())

# convert the object into a dict
validate_job_request_dict = validate_job_request_instance.to_dict()
# create an instance of ValidateJobRequest from a dict
validate_job_request_from_dict = ValidateJobRequest.from_dict(validate_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


