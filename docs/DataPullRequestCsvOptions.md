# DataPullRequestCsvOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **bool** |  | [optional] 
**separator** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 
**escape** | **str** |  | [optional] 
**null** | **str** |  | [optional] 
**force_null** | **List[str]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_pull_request_csv_options import DataPullRequestCsvOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DataPullRequestCsvOptions from a JSON string
data_pull_request_csv_options_instance = DataPullRequestCsvOptions.from_json(json)
# print the JSON string representation of the object
print(DataPullRequestCsvOptions.to_json())

# convert the object into a dict
data_pull_request_csv_options_dict = data_pull_request_csv_options_instance.to_dict()
# create an instance of DataPullRequestCsvOptions from a dict
data_pull_request_csv_options_from_dict = DataPullRequestCsvOptions.from_dict(data_pull_request_csv_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


