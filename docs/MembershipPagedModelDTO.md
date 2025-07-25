# MembershipPagedModelDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**content** | [**List[MembershipResponseDTO]**](MembershipResponseDTO.md) |  | [optional] 
**page** | [**PageDTO**](PageDTO.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.membership_paged_model_dto import MembershipPagedModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipPagedModelDTO from a JSON string
membership_paged_model_dto_instance = MembershipPagedModelDTO.from_json(json)
# print the JSON string representation of the object
print(MembershipPagedModelDTO.to_json())

# convert the object into a dict
membership_paged_model_dto_dict = membership_paged_model_dto_instance.to_dict()
# create an instance of MembershipPagedModelDTO from a dict
membership_paged_model_dto_from_dict = MembershipPagedModelDTO.from_dict(membership_paged_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


