# DwhMetricRangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DwhMetricRangeResponseContentInner]**](DwhMetricRangeResponseContentInner.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_metric_range_response import DwhMetricRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DwhMetricRangeResponse from a JSON string
dwh_metric_range_response_instance = DwhMetricRangeResponse.from_json(json)
# print the JSON string representation of the object
print(DwhMetricRangeResponse.to_json())

# convert the object into a dict
dwh_metric_range_response_dict = dwh_metric_range_response_instance.to_dict()
# create an instance of DwhMetricRangeResponse from a dict
dwh_metric_range_response_from_dict = DwhMetricRangeResponse.from_dict(dwh_metric_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


