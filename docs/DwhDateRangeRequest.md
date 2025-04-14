# DwhDateRangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_context** | [**ExecutionContext**](ExecutionContext.md) |  | [optional] 
**var_from** | **str** | defines the date property in a fact table | 
**filter** | [**DwhDateRangeRequestFilter**](DwhDateRangeRequestFilter.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_date_range_request import DwhDateRangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DwhDateRangeRequest from a JSON string
dwh_date_range_request_instance = DwhDateRangeRequest.from_json(json)
# print the JSON string representation of the object
print(DwhDateRangeRequest.to_json())

# convert the object into a dict
dwh_date_range_request_dict = dwh_date_range_request_instance.to_dict()
# create an instance of DwhDateRangeRequest from a dict
dwh_date_range_request_from_dict = DwhDateRangeRequest.from_dict(dwh_date_range_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


