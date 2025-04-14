# MembershipDTO


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
from cm_python_openapi_sdk.models.membership_dto import MembershipDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipDTO from a JSON string
membership_dto_instance = MembershipDTO.from_json(json)
# print the JSON string representation of the object
print(MembershipDTO.to_json())

# convert the object into a dict
membership_dto_dict = membership_dto_instance.to_dict()
# create an instance of MembershipDTO from a dict
membership_dto_from_dict = MembershipDTO.from_dict(membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


