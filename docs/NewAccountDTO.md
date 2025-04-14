# NewAccountDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**given_name** | **str** |  | 
**surname** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 
**consent_granted** | **bool** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**require_additional_attributes** | **bool** |  | [optional] 
**preferences** | [**AccountPreferences**](AccountPreferences.md) |  | [optional] 
**utm_parameters** | [**AccountUtmParameters**](AccountUtmParameters.md) |  | [optional] 
**job_info** | [**AccountJobInfo**](AccountJobInfo.md) |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.new_account_dto import NewAccountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NewAccountDTO from a JSON string
new_account_dto_instance = NewAccountDTO.from_json(json)
# print the JSON string representation of the object
print(NewAccountDTO.to_json())

# convert the object into a dict
new_account_dto_dict = new_account_dto_instance.to_dict()
# create an instance of NewAccountDTO from a dict
new_account_dto_from_dict = NewAccountDTO.from_dict(new_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


