# ImportProjectJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**ImportProjectRequest**](ImportProjectRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.import_project_job_request import ImportProjectJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProjectJobRequest from a JSON string
import_project_job_request_instance = ImportProjectJobRequest.from_json(json)
# print the JSON string representation of the object
print(ImportProjectJobRequest.to_json())

# convert the object into a dict
import_project_job_request_dict = import_project_job_request_instance.to_dict()
# create an instance of ImportProjectJobRequest from a dict
import_project_job_request_from_dict = ImportProjectJobRequest.from_dict(import_project_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


