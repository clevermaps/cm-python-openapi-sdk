# ProjectResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**status** | **str** |  | 
**share** | **str** |  | 
**created_at** | **str** |  | 
**modified_at** | **str** |  | [optional] 
**membership** | [**MembershipDTO**](MembershipDTO.md) |  | [optional] 
**services** | **object** |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | 

## Example

```python
from cm_python_openapi_sdk.models.project_response_dto import ProjectResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseDTO from a JSON string
project_response_dto_instance = ProjectResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectResponseDTO.to_json())

# convert the object into a dict
project_response_dto_dict = project_response_dto_instance.to_dict()
# create an instance of ProjectResponseDTO from a dict
project_response_dto_from_dict = ProjectResponseDTO.from_dict(project_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


