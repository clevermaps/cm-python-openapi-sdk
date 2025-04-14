# AccountOnboardingParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intro_shown** | **List[str]** |  | [optional] 
**tips_shown** | **List[str]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.account_onboarding_parameters import AccountOnboardingParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOnboardingParameters from a JSON string
account_onboarding_parameters_instance = AccountOnboardingParameters.from_json(json)
# print the JSON string representation of the object
print(AccountOnboardingParameters.to_json())

# convert the object into a dict
account_onboarding_parameters_dict = account_onboarding_parameters_instance.to_dict()
# create an instance of AccountOnboardingParameters from a dict
account_onboarding_parameters_from_dict = AccountOnboardingParameters.from_dict(account_onboarding_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


