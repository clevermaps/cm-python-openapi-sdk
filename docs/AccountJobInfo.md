# AccountJobInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**job_position** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.account_job_info import AccountJobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountJobInfo from a JSON string
account_job_info_instance = AccountJobInfo.from_json(json)
# print the JSON string representation of the object
print(AccountJobInfo.to_json())

# convert the object into a dict
account_job_info_dict = account_job_info_instance.to_dict()
# create an instance of AccountJobInfo from a dict
account_job_info_from_dict = AccountJobInfo.from_dict(account_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


