# BulkPointQueryRequestPointQueriesNearest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [optional] 
**type** | **str** |  | 
**options** | [**BulkPointQueryPointQueriesOptionNearest**](BulkPointQueryPointQueriesOptionNearest.md) |  | 
**dataset** | **str** |  | 
**execution_content** | **object** |  | [optional] 
**properties** | **List[object]** |  | [optional] 
**filter_by** | **List[object]** |  | [optional] 
**result_set_filter** | **List[object]** |  | [optional] 
**having** | **List[object]** |  | [optional] 
**order_by** | **List[object]** |  | [optional] 
**variables** | **List[object]** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.bulk_point_query_request_point_queries_nearest import BulkPointQueryRequestPointQueriesNearest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPointQueryRequestPointQueriesNearest from a JSON string
bulk_point_query_request_point_queries_nearest_instance = BulkPointQueryRequestPointQueriesNearest.from_json(json)
# print the JSON string representation of the object
print(BulkPointQueryRequestPointQueriesNearest.to_json())

# convert the object into a dict
bulk_point_query_request_point_queries_nearest_dict = bulk_point_query_request_point_queries_nearest_instance.to_dict()
# create an instance of BulkPointQueryRequestPointQueriesNearest from a dict
bulk_point_query_request_point_queries_nearest_from_dict = BulkPointQueryRequestPointQueriesNearest.from_dict(bulk_point_query_request_point_queries_nearest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


