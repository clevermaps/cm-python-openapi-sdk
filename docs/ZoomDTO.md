# ZoomDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | 
**optimal** | **int** |  | 
**max** | **int** |  | 
**visible_from** | **int** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.zoom_dto import ZoomDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ZoomDTO from a JSON string
zoom_dto_instance = ZoomDTO.from_json(json)
# print the JSON string representation of the object
print(ZoomDTO.to_json())

# convert the object into a dict
zoom_dto_dict = zoom_dto_instance.to_dict()
# create an instance of ZoomDTO from a dict
zoom_dto_from_dict = ZoomDTO.from_dict(zoom_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


