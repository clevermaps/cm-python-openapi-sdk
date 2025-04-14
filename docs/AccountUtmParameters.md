# AccountUtmParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**campaign** | **str** |  | [optional] 
**referrer** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.account_utm_parameters import AccountUtmParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUtmParameters from a JSON string
account_utm_parameters_instance = AccountUtmParameters.from_json(json)
# print the JSON string representation of the object
print(AccountUtmParameters.to_json())

# convert the object into a dict
account_utm_parameters_dict = account_utm_parameters_instance.to_dict()
# create an instance of AccountUtmParameters from a dict
account_utm_parameters_from_dict = AccountUtmParameters.from_dict(account_utm_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


