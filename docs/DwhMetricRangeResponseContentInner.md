# DwhMetricRangeResponseContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** |  | [optional] 
**min** | **object** |  | [optional] 
**max** | **object** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_metric_range_response_content_inner import DwhMetricRangeResponseContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of DwhMetricRangeResponseContentInner from a JSON string
dwh_metric_range_response_content_inner_instance = DwhMetricRangeResponseContentInner.from_json(json)
# print the JSON string representation of the object
print(DwhMetricRangeResponseContentInner.to_json())

# convert the object into a dict
dwh_metric_range_response_content_inner_dict = dwh_metric_range_response_content_inner_instance.to_dict()
# create an instance of DwhMetricRangeResponseContentInner from a dict
dwh_metric_range_response_content_inner_from_dict = DwhMetricRangeResponseContentInner.from_dict(dwh_metric_range_response_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


