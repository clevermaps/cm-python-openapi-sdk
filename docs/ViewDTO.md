# ViewDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | 
**content** | [**ViewContentDTO**](ViewContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.view_dto import ViewDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDTO from a JSON string
view_dto_instance = ViewDTO.from_json(json)
# print the JSON string representation of the object
print(ViewDTO.to_json())

# convert the object into a dict
view_dto_dict = view_dto_instance.to_dict()
# create an instance of ViewDTO from a dict
view_dto_from_dict = ViewDTO.from_dict(view_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


