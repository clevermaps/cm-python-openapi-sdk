# DwhPropertyValuesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_context** | [**ExecutionContext**](ExecutionContext.md) |  | [optional] 
**var_property** | **str** | identifier of a property from data model | 
**filter** | **str** | substring filter of the property values. Only property values containing given string will be returned. Filtering is case insensitive. | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_property_values_request import DwhPropertyValuesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DwhPropertyValuesRequest from a JSON string
dwh_property_values_request_instance = DwhPropertyValuesRequest.from_json(json)
# print the JSON string representation of the object
print(DwhPropertyValuesRequest.to_json())

# convert the object into a dict
dwh_property_values_request_dict = dwh_property_values_request_instance.to_dict()
# create an instance of DwhPropertyValuesRequest from a dict
dwh_property_values_request_from_dict = DwhPropertyValuesRequest.from_dict(dwh_property_values_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


