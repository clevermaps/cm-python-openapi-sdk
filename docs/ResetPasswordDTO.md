# ResetPasswordDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | 
**consent_granted** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.reset_password_dto import ResetPasswordDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordDTO from a JSON string
reset_password_dto_instance = ResetPasswordDTO.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordDTO.to_json())

# convert the object into a dict
reset_password_dto_dict = reset_password_dto_instance.to_dict()
# create an instance of ResetPasswordDTO from a dict
reset_password_dto_from_dict = ResetPasswordDTO.from_dict(reset_password_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


