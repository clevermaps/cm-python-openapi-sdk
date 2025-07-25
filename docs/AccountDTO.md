# AccountDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**full_name** | **str** |  | 
**email** | **str** |  | 
**consent_granted** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**anonymous** | **bool** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**preferences** | [**AccountPreferences**](AccountPreferences.md) |  | [optional] 
**onboarding** | [**AccountOnboardingParameters**](AccountOnboardingParameters.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.account_dto import AccountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDTO from a JSON string
account_dto_instance = AccountDTO.from_json(json)
# print the JSON string representation of the object
print(AccountDTO.to_json())

# convert the object into a dict
account_dto_dict = account_dto_instance.to_dict()
# create an instance of AccountDTO from a dict
account_dto_from_dict = AccountDTO.from_dict(account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


