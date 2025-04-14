# AccountPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional] 
**last_active_project** | **str** |  | [optional] 
**last_active_organization** | **str** |  | [optional] 
**send_newsletter** | **bool** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.account_preferences import AccountPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPreferences from a JSON string
account_preferences_instance = AccountPreferences.from_json(json)
# print the JSON string representation of the object
print(AccountPreferences.to_json())

# convert the object into a dict
account_preferences_dict = account_preferences_instance.to_dict()
# create an instance of AccountPreferences from a dict
account_preferences_from_dict = AccountPreferences.from_dict(account_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


