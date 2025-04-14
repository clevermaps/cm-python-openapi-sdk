# SendResetPasswordDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.send_reset_password_dto import SendResetPasswordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SendResetPasswordDTO from a JSON string
send_reset_password_dto_instance = SendResetPasswordDTO.from_json(json)
# print the JSON string representation of the object
print(SendResetPasswordDTO.to_json())

# convert the object into a dict
send_reset_password_dto_dict = send_reset_password_dto_instance.to_dict()
# create an instance of SendResetPasswordDTO from a dict
send_reset_password_dto_from_dict = SendResetPasswordDTO.from_dict(send_reset_password_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


