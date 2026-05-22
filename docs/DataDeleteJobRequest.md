# DataDeleteJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**DataDeleteRequest**](DataDeleteRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_delete_job_request import DataDeleteJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataDeleteJobRequest from a JSON string
data_delete_job_request_instance = DataDeleteJobRequest.from_json(json)
# print the JSON string representation of the object
print(DataDeleteJobRequest.to_json())

# convert the object into a dict
data_delete_job_request_dict = data_delete_job_request_instance.to_dict()
# create an instance of DataDeleteJobRequest from a dict
data_delete_job_request_from_dict = DataDeleteJobRequest.from_dict(data_delete_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


