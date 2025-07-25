# GeneralJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**ImportProjectRequest**](ImportProjectRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.general_job_request import GeneralJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralJobRequest from a JSON string
general_job_request_instance = GeneralJobRequest.from_json(json)
# print the JSON string representation of the object
print(GeneralJobRequest.to_json())

# convert the object into a dict
general_job_request_dict = general_job_request_instance.to_dict()
# create an instance of GeneralJobRequest from a dict
general_job_request_from_dict = GeneralJobRequest.from_dict(general_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


