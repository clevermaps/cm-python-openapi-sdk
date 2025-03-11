# CreateOrganizationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**invitation_email** | **str** |  | [optional] 
**dwh_cluster_id** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.create_organization_dto import CreateOrganizationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationDTO from a JSON string
create_organization_dto_instance = CreateOrganizationDTO.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationDTO.to_json())

# convert the object into a dict
create_organization_dto_dict = create_organization_dto_instance.to_dict()
# create an instance of CreateOrganizationDTO from a dict
create_organization_dto_from_dict = CreateOrganizationDTO.from_dict(create_organization_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


