# DwhQueryMetricType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**metric** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_query_metric_type import DwhQueryMetricType

# TODO update the JSON string below
json = "{}"
# create an instance of DwhQueryMetricType from a JSON string
dwh_query_metric_type_instance = DwhQueryMetricType.from_json(json)
# print the JSON string representation of the object
print(DwhQueryMetricType.to_json())

# convert the object into a dict
dwh_query_metric_type_dict = dwh_query_metric_type_instance.to_dict()
# create an instance of DwhQueryMetricType from a dict
dwh_query_metric_type_from_dict = DwhQueryMetricType.from_dict(dwh_query_metric_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


