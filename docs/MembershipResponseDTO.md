# MembershipResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**status** | **str** |  | 
**role** | **str** |  | 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**account** | [**AccountDTO**](AccountDTO.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.membership_response_dto import MembershipResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipResponseDTO from a JSON string
membership_response_dto_instance = MembershipResponseDTO.from_json(json)
# print the JSON string representation of the object
print(MembershipResponseDTO.to_json())

# convert the object into a dict
membership_response_dto_dict = membership_response_dto_instance.to_dict()
# create an instance of MembershipResponseDTO from a dict
membership_response_dto_from_dict = MembershipResponseDTO.from_dict(membership_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


