# CreateMembershipDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**role** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.create_membership_dto import CreateMembershipDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMembershipDTO from a JSON string
create_membership_dto_instance = CreateMembershipDTO.from_json(json)
# print the JSON string representation of the object
print(CreateMembershipDTO.to_json())

# convert the object into a dict
create_membership_dto_dict = create_membership_dto_instance.to_dict()
# create an instance of CreateMembershipDTO from a dict
create_membership_dto_from_dict = CreateMembershipDTO.from_dict(create_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


