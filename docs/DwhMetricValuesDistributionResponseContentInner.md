# DwhMetricValuesDistributionResponseContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**content** | [**List[DwhMetricValuesDistributionResponseContentInnerContentInner]**](DwhMetricValuesDistributionResponseContentInnerContentInner.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_response_content_inner import DwhMetricValuesDistributionResponseContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of DwhMetricValuesDistributionResponseContentInner from a JSON string
dwh_metric_values_distribution_response_content_inner_instance = DwhMetricValuesDistributionResponseContentInner.from_json(json)
# print the JSON string representation of the object
print(DwhMetricValuesDistributionResponseContentInner.to_json())

# convert the object into a dict
dwh_metric_values_distribution_response_content_inner_dict = dwh_metric_values_distribution_response_content_inner_instance.to_dict()
# create an instance of DwhMetricValuesDistributionResponseContentInner from a dict
dwh_metric_values_distribution_response_content_inner_from_dict = DwhMetricValuesDistributionResponseContentInner.from_dict(dwh_metric_values_distribution_response_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


