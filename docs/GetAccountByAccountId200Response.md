# GetAccountByAccountId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**full_name** | **str** |  | 
**email** | **str** |  | 
**status** | **str** |  | 
**preferences** | [**AccountPreferences**](AccountPreferences.md) |  | [optional] 
**consent_granted** | **bool** |  | [optional] 
**anonymous** | **bool** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**onboarding** | [**AccountOnboardingParameters**](AccountOnboardingParameters.md) |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.get_account_by_account_id200_response import GetAccountByAccountId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountByAccountId200Response from a JSON string
get_account_by_account_id200_response_instance = GetAccountByAccountId200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountByAccountId200Response.to_json())

# convert the object into a dict
get_account_by_account_id200_response_dict = get_account_by_account_id200_response_instance.to_dict()
# create an instance of GetAccountByAccountId200Response from a dict
get_account_by_account_id200_response_from_dict = GetAccountByAccountId200Response.from_dict(get_account_by_account_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


