# UpdateMembershipDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.update_membership_dto import UpdateMembershipDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembershipDTO from a JSON string
update_membership_dto_instance = UpdateMembershipDTO.from_json(json)
# print the JSON string representation of the object
print(UpdateMembershipDTO.to_json())

# convert the object into a dict
update_membership_dto_dict = update_membership_dto_instance.to_dict()
# create an instance of UpdateMembershipDTO from a dict
update_membership_dto_from_dict = UpdateMembershipDTO.from_dict(update_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


