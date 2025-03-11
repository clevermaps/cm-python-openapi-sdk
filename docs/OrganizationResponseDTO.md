# OrganizationResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**invitation_email** | **str** |  | [optional] 
**dwh_cluster_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.organization_response_dto import OrganizationResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResponseDTO from a JSON string
organization_response_dto_instance = OrganizationResponseDTO.from_json(json)
# print the JSON string representation of the object
print(OrganizationResponseDTO.to_json())

# convert the object into a dict
organization_response_dto_dict = organization_response_dto_instance.to_dict()
# create an instance of OrganizationResponseDTO from a dict
organization_response_dto_from_dict = OrganizationResponseDTO.from_dict(organization_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


