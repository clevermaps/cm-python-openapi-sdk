# JobDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**start_date** | **object** |  | [optional] 
**end_date** | **object** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **object** |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.job_detail_response import JobDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobDetailResponse from a JSON string
job_detail_response_instance = JobDetailResponse.from_json(json)
# print the JSON string representation of the object
print(JobDetailResponse.to_json())

# convert the object into a dict
job_detail_response_dict = job_detail_response_instance.to_dict()
# create an instance of JobDetailResponse from a dict
job_detail_response_from_dict = JobDetailResponse.from_dict(job_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


