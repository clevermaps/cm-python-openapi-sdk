# CreateInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.create_invitation import CreateInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvitation from a JSON string
create_invitation_instance = CreateInvitation.from_json(json)
# print the JSON string representation of the object
print(CreateInvitation.to_json())

# convert the object into a dict
create_invitation_dict = create_invitation_instance.to_dict()
# create an instance of CreateInvitation from a dict
create_invitation_from_dict = CreateInvitation.from_dict(create_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


