# UpdateMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.update_membership import UpdateMembership

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembership from a JSON string
update_membership_instance = UpdateMembership.from_json(json)
# print the JSON string representation of the object
print(UpdateMembership.to_json())

# convert the object into a dict
update_membership_dict = update_membership_instance.to_dict()
# create an instance of UpdateMembership from a dict
update_membership_from_dict = UpdateMembership.from_dict(update_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


