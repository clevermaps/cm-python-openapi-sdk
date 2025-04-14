# DwhOverlapsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[DwhOverlapsResponseContentInner]**](DwhOverlapsResponseContentInner.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_overlaps_response import DwhOverlapsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DwhOverlapsResponse from a JSON string
dwh_overlaps_response_instance = DwhOverlapsResponse.from_json(json)
# print the JSON string representation of the object
print(DwhOverlapsResponse.to_json())

# convert the object into a dict
dwh_overlaps_response_dict = dwh_overlaps_response_instance.to_dict()
# create an instance of DwhOverlapsResponse from a dict
dwh_overlaps_response_from_dict = DwhOverlapsResponse.from_dict(dwh_overlaps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


