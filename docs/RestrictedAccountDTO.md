# RestrictedAccountDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**full_name** | **str** |  | 
**email** | **str** |  | 
**status** | **str** |  | 
**preferences** | [**AccountPreferences**](AccountPreferences.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.restricted_account_dto import RestrictedAccountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedAccountDTO from a JSON string
restricted_account_dto_instance = RestrictedAccountDTO.from_json(json)
# print the JSON string representation of the object
print(RestrictedAccountDTO.to_json())

# convert the object into a dict
restricted_account_dto_dict = restricted_account_dto_instance.to_dict()
# create an instance of RestrictedAccountDTO from a dict
restricted_account_dto_from_dict = RestrictedAccountDTO.from_dict(restricted_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


