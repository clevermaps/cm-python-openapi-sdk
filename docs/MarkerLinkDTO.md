# MarkerLinkDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marker** | **str** |  | 
**visible** | **bool** |  | [default to True]
**add_on_expand** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.marker_link_dto import MarkerLinkDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerLinkDTO from a JSON string
marker_link_dto_instance = MarkerLinkDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerLinkDTO.to_json())

# convert the object into a dict
marker_link_dto_dict = marker_link_dto_instance.to_dict()
# create an instance of MarkerLinkDTO from a dict
marker_link_dto_from_dict = MarkerLinkDTO.from_dict(marker_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


