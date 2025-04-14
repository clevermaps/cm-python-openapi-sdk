# DwhPropertyValuesDistributionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_context** | [**ExecutionContext**](ExecutionContext.md) |  | [optional] 
**var_property** | **str** |  | 
**buckets** | **int** |  | [optional] [default to 20]
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_property_values_distribution_request import DwhPropertyValuesDistributionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DwhPropertyValuesDistributionRequest from a JSON string
dwh_property_values_distribution_request_instance = DwhPropertyValuesDistributionRequest.from_json(json)
# print the JSON string representation of the object
print(DwhPropertyValuesDistributionRequest.to_json())

# convert the object into a dict
dwh_property_values_distribution_request_dict = dwh_property_values_distribution_request_instance.to_dict()
# create an instance of DwhPropertyValuesDistributionRequest from a dict
dwh_property_values_distribution_request_from_dict = DwhPropertyValuesDistributionRequest.from_dict(dwh_property_values_distribution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


