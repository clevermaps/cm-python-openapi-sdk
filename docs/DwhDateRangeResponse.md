# DwhDateRangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DwhDateRangeResponseContentInner]**](DwhDateRangeResponseContentInner.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_date_range_response import DwhDateRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DwhDateRangeResponse from a JSON string
dwh_date_range_response_instance = DwhDateRangeResponse.from_json(json)
# print the JSON string representation of the object
print(DwhDateRangeResponse.to_json())

# convert the object into a dict
dwh_date_range_response_dict = dwh_date_range_response_instance.to_dict()
# create an instance of DwhDateRangeResponse from a dict
dwh_date_range_response_from_dict = DwhDateRangeResponse.from_dict(dwh_date_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


