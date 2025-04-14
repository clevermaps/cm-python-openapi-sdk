# DwhOverlapsResponseContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** |  | [optional] 
**results** | [**List[DwhOverlapsResponseContentInnerResultsInner]**](DwhOverlapsResponseContentInnerResultsInner.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.dwh_overlaps_response_content_inner import DwhOverlapsResponseContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of DwhOverlapsResponseContentInner from a JSON string
dwh_overlaps_response_content_inner_instance = DwhOverlapsResponseContentInner.from_json(json)
# print the JSON string representation of the object
print(DwhOverlapsResponseContentInner.to_json())

# convert the object into a dict
dwh_overlaps_response_content_inner_dict = dwh_overlaps_response_content_inner_instance.to_dict()
# create an instance of DwhOverlapsResponseContentInner from a dict
dwh_overlaps_response_content_inner_from_dict = DwhOverlapsResponseContentInner.from_dict(dwh_overlaps_response_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


