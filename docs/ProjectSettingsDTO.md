# ProjectSettingsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | [**ProjectSettingsContentDTO**](ProjectSettingsContentDTO.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.project_settings_dto import ProjectSettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSettingsDTO from a JSON string
project_settings_dto_instance = ProjectSettingsDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectSettingsDTO.to_json())

# convert the object into a dict
project_settings_dto_dict = project_settings_dto_instance.to_dict()
# create an instance of ProjectSettingsDTO from a dict
project_settings_dto_from_dict = ProjectSettingsDTO.from_dict(project_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


