# ExportContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **List[str]** |  | [optional] 
**output** | [**OutputDTO**](OutputDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.export_content_dto import ExportContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExportContentDTO from a JSON string
export_content_dto_instance = ExportContentDTO.from_json(json)
# print the JSON string representation of the object
print(ExportContentDTO.to_json())

# convert the object into a dict
export_content_dto_dict = export_content_dto_instance.to_dict()
# create an instance of ExportContentDTO from a dict
export_content_dto_from_dict = ExportContentDTO.from_dict(export_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


