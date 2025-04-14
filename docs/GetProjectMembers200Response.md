# GetProjectMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[MembershipDTO]**](MembershipDTO.md) |  | [optional] 
**page** | [**MandatoryKeysForPagableResponse**](MandatoryKeysForPagableResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**status** | **str** |  | 
**role** | **str** |  | 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**account** | [**AccountDTO**](AccountDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.get_project_members200_response import GetProjectMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectMembers200Response from a JSON string
get_project_members200_response_instance = GetProjectMembers200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectMembers200Response.to_json())

# convert the object into a dict
get_project_members200_response_dict = get_project_members200_response_instance.to_dict()
# create an instance of GetProjectMembers200Response from a dict
get_project_members200_response_from_dict = GetProjectMembers200Response.from_dict(get_project_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


