# JobHistoryPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | **List[object]** |  | [optional] 
**page** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.job_history_paged_model_dto import JobHistoryPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JobHistoryPagedModelDTO from a JSON string
job_history_paged_model_dto_instance = JobHistoryPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(JobHistoryPagedModelDTO.to_json())

# convert the object into a dict
job_history_paged_model_dto_dict = job_history_paged_model_dto_instance.to_dict()
# create an instance of JobHistoryPagedModelDTO from a dict
job_history_paged_model_dto_from_dict = JobHistoryPagedModelDTO.from_dict(job_history_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


