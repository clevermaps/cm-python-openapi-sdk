# GetOrganizations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[OrganizationResponseDTO]**](OrganizationResponseDTO.md) |  | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**invitation_email** | **str** |  | [optional] 
**dwh_cluster_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.get_organizations200_response import GetOrganizations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizations200Response from a JSON string
get_organizations200_response_instance = GetOrganizations200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganizations200Response.to_json())

# convert the object into a dict
get_organizations200_response_dict = get_organizations200_response_instance.to_dict()
# create an instance of GetOrganizations200Response from a dict
get_organizations200_response_from_dict = GetOrganizations200Response.from_dict(get_organizations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


