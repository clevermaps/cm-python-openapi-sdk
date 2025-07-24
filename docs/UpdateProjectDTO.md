# UpdateProjectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**services** | [**ProjectResponseDTOServices**](ProjectResponseDTOServices.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.update_project_dto import UpdateProjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectDTO from a JSON string
update_project_dto_instance = UpdateProjectDTO.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectDTO.to_json())

# convert the object into a dict
update_project_dto_dict = update_project_dto_instance.to_dict()
# create an instance of UpdateProjectDTO from a dict
update_project_dto_from_dict = UpdateProjectDTO.from_dict(update_project_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


