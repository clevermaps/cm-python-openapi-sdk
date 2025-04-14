# DwhDateRangeResponseContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**filtered** | **bool** |  | [optional] 
**min** | **str** |  | [optional] 
**max** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_date_range_response_content_inner import DwhDateRangeResponseContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of DwhDateRangeResponseContentInner from a JSON string
dwh_date_range_response_content_inner_instance = DwhDateRangeResponseContentInner.from_json(json)
# print the JSON string representation of the object
print(DwhDateRangeResponseContentInner.to_json())

# convert the object into a dict
dwh_date_range_response_content_inner_dict = dwh_date_range_response_content_inner_instance.to_dict()
# create an instance of DwhDateRangeResponseContentInner from a dict
dwh_date_range_response_content_inner_from_dict = DwhDateRangeResponseContentInner.from_dict(dwh_date_range_response_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


