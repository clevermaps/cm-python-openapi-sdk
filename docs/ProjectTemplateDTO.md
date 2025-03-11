# ProjectTemplateDTO

Object containing properties related to project templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_datasets** | [**List[TemplateDatasetDTO]**](TemplateDatasetDTO.md) | Array of links to datasets which will be marked as available to load with custom data. | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.project_template_dto import ProjectTemplateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateDTO from a JSON string
project_template_dto_instance = ProjectTemplateDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateDTO.to_json())

# convert the object into a dict
project_template_dto_dict = project_template_dto_instance.to_dict()
# create an instance of ProjectTemplateDTO from a dict
project_template_dto_from_dict = ProjectTemplateDTO.from_dict(project_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


