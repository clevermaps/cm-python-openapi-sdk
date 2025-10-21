# DwhMetricValuesDistributionResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DwhMetricValuesDistributionResponseContentInner]**](DwhMetricValuesDistributionResponseContentInner.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_response1 import DwhMetricValuesDistributionResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of DwhMetricValuesDistributionResponse1 from a JSON string
dwh_metric_values_distribution_response1_instance = DwhMetricValuesDistributionResponse1.from_json(json)
# print the JSON string representation of the object
print(DwhMetricValuesDistributionResponse1.to_json())

# convert the object into a dict
dwh_metric_values_distribution_response1_dict = dwh_metric_values_distribution_response1_instance.to_dict()
# create an instance of DwhMetricValuesDistributionResponse1 from a dict
dwh_metric_values_distribution_response1_from_dict = DwhMetricValuesDistributionResponse1.from_dict(dwh_metric_values_distribution_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


