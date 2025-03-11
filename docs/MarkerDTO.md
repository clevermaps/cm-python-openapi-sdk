# MarkerDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | [**MarkerContentDTO**](MarkerContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.marker_dto import MarkerDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerDTO from a JSON string
marker_dto_instance = MarkerDTO.from_json(json)
# print the JSON string representation of the object
print(MarkerDTO.to_json())

# convert the object into a dict
marker_dto_dict = marker_dto_instance.to_dict()
# create an instance of MarkerDTO from a dict
marker_dto_from_dict = MarkerDTO.from_dict(marker_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


