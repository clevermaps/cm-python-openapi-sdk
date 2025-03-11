# ProjectSettingsContentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_search_countries** | **List[str]** | Array of country codes, as defined by ISO 3166 alpha-2, to limit the geographical search. | [optional] 
**geo_search_providers** | **List[str]** | Array of geographical search providers. | [default to [Mapbox]]
**project_template** | [**ProjectTemplateDTO**](ProjectTemplateDTO.md) |  | [optional] 
**trusted_origins** | **List[str]** |  | [optional] 
**allow_unsecured_origins** | **bool** |  | [optional] [default to False]
**default_views** | **List[str]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.project_settings_content_dto import ProjectSettingsContentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSettingsContentDTO from a JSON string
project_settings_content_dto_instance = ProjectSettingsContentDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectSettingsContentDTO.to_json())

# convert the object into a dict
project_settings_content_dto_dict = project_settings_content_dto_instance.to_dict()
# create an instance of ProjectSettingsContentDTO from a dict
project_settings_content_dto_from_dict = ProjectSettingsContentDTO.from_dict(project_settings_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


