# PasswordChangeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.password_change_dto import PasswordChangeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordChangeDTO from a JSON string
password_change_dto_instance = PasswordChangeDTO.from_json(json)
# print the JSON string representation of the object
print(PasswordChangeDTO.to_json())

# convert the object into a dict
password_change_dto_dict = password_change_dto_instance.to_dict()
# create an instance of PasswordChangeDTO from a dict
password_change_dto_from_dict = PasswordChangeDTO.from_dict(password_change_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


