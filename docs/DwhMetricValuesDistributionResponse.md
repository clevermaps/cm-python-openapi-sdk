# DwhMetricValuesDistributionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DwhMetricValuesDistributionResponseContentInner]**](DwhMetricValuesDistributionResponseContentInner.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_response import DwhMetricValuesDistributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DwhMetricValuesDistributionResponse from a JSON string
dwh_metric_values_distribution_response_instance = DwhMetricValuesDistributionResponse.from_json(json)
# print the JSON string representation of the object
print(DwhMetricValuesDistributionResponse.to_json())

# convert the object into a dict
dwh_metric_values_distribution_response_dict = dwh_metric_values_distribution_response_instance.to_dict()
# create an instance of DwhMetricValuesDistributionResponse from a dict
dwh_metric_values_distribution_response_from_dict = DwhMetricValuesDistributionResponse.from_dict(dwh_metric_values_distribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


