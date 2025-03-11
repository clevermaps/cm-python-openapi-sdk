# BulkPointQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_billing** | **bool** |  | [optional] 
**points** | [**List[BulkPointQueryRequestPointsInner]**](BulkPointQueryRequestPointsInner.md) |  | 
**point_queries** | [**List[BulkPointQueryRequestPointQueriesInner]**](BulkPointQueryRequestPointQueriesInner.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.bulk_point_query_request import BulkPointQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPointQueryRequest from a JSON string
bulk_point_query_request_instance = BulkPointQueryRequest.from_json(json)
# print the JSON string representation of the object
print(BulkPointQueryRequest.to_json())

# convert the object into a dict
bulk_point_query_request_dict = bulk_point_query_request_instance.to_dict()
# create an instance of BulkPointQueryRequest from a dict
bulk_point_query_request_from_dict = BulkPointQueryRequest.from_dict(bulk_point_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


