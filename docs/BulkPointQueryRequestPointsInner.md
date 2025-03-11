# BulkPointQueryRequestPointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**lat** | **float** |  | 
**lng** | **float** |  | 

## Example

```python
from cm_python_openapi_sdk.models.bulk_point_query_request_points_inner import BulkPointQueryRequestPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPointQueryRequestPointsInner from a JSON string
bulk_point_query_request_points_inner_instance = BulkPointQueryRequestPointsInner.from_json(json)
# print the JSON string representation of the object
print(BulkPointQueryRequestPointsInner.to_json())

# convert the object into a dict
bulk_point_query_request_points_inner_dict = bulk_point_query_request_points_inner_instance.to_dict()
# create an instance of BulkPointQueryRequestPointsInner from a dict
bulk_point_query_request_points_inner_from_dict = BulkPointQueryRequestPointsInner.from_dict(bulk_point_query_request_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


