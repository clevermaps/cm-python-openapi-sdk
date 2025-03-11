# BulkPointQueryJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_id** | **str** |  | 
**content** | [**BulkPointQueryRequest**](BulkPointQueryRequest.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.bulk_point_query_job_request import BulkPointQueryJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPointQueryJobRequest from a JSON string
bulk_point_query_job_request_instance = BulkPointQueryJobRequest.from_json(json)
# print the JSON string representation of the object
print(BulkPointQueryJobRequest.to_json())

# convert the object into a dict
bulk_point_query_job_request_dict = bulk_point_query_job_request_instance.to_dict()
# create an instance of BulkPointQueryJobRequest from a dict
bulk_point_query_job_request_from_dict = BulkPointQueryJobRequest.from_dict(bulk_point_query_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


