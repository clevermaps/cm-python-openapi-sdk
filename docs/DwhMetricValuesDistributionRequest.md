# DwhMetricValuesDistributionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | **int** |  | [optional] 
**breakpoints** | **List[float]** |  | [optional] 
**query** | [**DwhQueryRequest1**](DwhQueryRequest1.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_request import DwhMetricValuesDistributionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DwhMetricValuesDistributionRequest from a JSON string
dwh_metric_values_distribution_request_instance = DwhMetricValuesDistributionRequest.from_json(json)
# print the JSON string representation of the object
print(DwhMetricValuesDistributionRequest.to_json())

# convert the object into a dict
dwh_metric_values_distribution_request_dict = dwh_metric_values_distribution_request_instance.to_dict()
# create an instance of DwhMetricValuesDistributionRequest from a dict
dwh_metric_values_distribution_request_from_dict = DwhMetricValuesDistributionRequest.from_dict(dwh_metric_values_distribution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


