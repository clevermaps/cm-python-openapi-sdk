# ExportDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**ExportContentDTO**](ExportContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.export_dto import ExportDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExportDTO from a JSON string
export_dto_instance = ExportDTO.from_json(json)
# print the JSON string representation of the object
print(ExportDTO.to_json())

# convert the object into a dict
export_dto_dict = export_dto_instance.to_dict()
# create an instance of ExportDTO from a dict
export_dto_from_dict = ExportDTO.from_dict(export_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


