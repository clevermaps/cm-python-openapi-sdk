# DwhOverlapsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operators** | **List[str]** |  | 
**objects** | [**List[FilterBy]**](FilterBy.md) |  | 
**granularity** | **str** |  | 
**query** | [**DwhQueryRequest1**](DwhQueryRequest1.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.dwh_overlaps_request import DwhOverlapsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DwhOverlapsRequest from a JSON string
dwh_overlaps_request_instance = DwhOverlapsRequest.from_json(json)
# print the JSON string representation of the object
print(DwhOverlapsRequest.to_json())

# convert the object into a dict
dwh_overlaps_request_dict = dwh_overlaps_request_instance.to_dict()
# create an instance of DwhOverlapsRequest from a dict
dwh_overlaps_request_from_dict = DwhOverlapsRequest.from_dict(dwh_overlaps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


