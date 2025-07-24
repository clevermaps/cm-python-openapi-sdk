# ProjectPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[ProjectResponseDTO]**](ProjectResponseDTO.md) |  | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.project_paged_model_dto import ProjectPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPagedModelDTO from a JSON string
project_paged_model_dto_instance = ProjectPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectPagedModelDTO.to_json())

# convert the object into a dict
project_paged_model_dto_dict = project_paged_model_dto_instance.to_dict()
# create an instance of ProjectPagedModelDTO from a dict
project_paged_model_dto_from_dict = ProjectPagedModelDTO.from_dict(project_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


