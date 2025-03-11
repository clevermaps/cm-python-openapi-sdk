# InvitationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | 
**status** | **str** |  | 
**role** | **str** |  | 
**created_at** | **str** |  | 
**modified_at** | **str** |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.invitation_dto import InvitationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationDTO from a JSON string
invitation_dto_instance = InvitationDTO.from_json(json)
# print the JSON string representation of the object
print(InvitationDTO.to_json())

# convert the object into a dict
invitation_dto_dict = invitation_dto_instance.to_dict()
# create an instance of InvitationDTO from a dict
invitation_dto_from_dict = InvitationDTO.from_dict(invitation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


