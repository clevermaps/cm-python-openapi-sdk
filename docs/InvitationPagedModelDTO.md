# InvitationPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[InvitationDTO]**](InvitationDTO.md) |  | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.invitation_paged_model_dto import InvitationPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationPagedModelDTO from a JSON string
invitation_paged_model_dto_instance = InvitationPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(InvitationPagedModelDTO.to_json())

# convert the object into a dict
invitation_paged_model_dto_dict = invitation_paged_model_dto_instance.to_dict()
# create an instance of InvitationPagedModelDTO from a dict
invitation_paged_model_dto_from_dict = InvitationPagedModelDTO.from_dict(invitation_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


