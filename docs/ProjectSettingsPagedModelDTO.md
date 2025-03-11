# ProjectSettingsPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ProjectSettingsDTO]**](ProjectSettingsDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.project_settings_paged_model_dto import ProjectSettingsPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSettingsPagedModelDTO from a JSON string
project_settings_paged_model_dto_instance = ProjectSettingsPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectSettingsPagedModelDTO.to_json())

# convert the object into a dict
project_settings_paged_model_dto_dict = project_settings_paged_model_dto_instance.to_dict()
# create an instance of ProjectSettingsPagedModelDTO from a dict
project_settings_paged_model_dto_from_dict = ProjectSettingsPagedModelDTO.from_dict(project_settings_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


