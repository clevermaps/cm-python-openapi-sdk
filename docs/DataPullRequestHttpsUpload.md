# DataPullRequestHttpsUpload

Object specifying properties for dataPull from any HTTPS URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | HTTPS URL (e.g. https://can-s3-dwh-pull-test.s3-eu-west-1.amazonaws.com/shops.csv). | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_pull_request_https_upload import DataPullRequestHttpsUpload

# TODO update the JSON string below
json = "{}"
# create an instance of DataPullRequestHttpsUpload from a JSON string
data_pull_request_https_upload_instance = DataPullRequestHttpsUpload.from_json(json)
# print the JSON string representation of the object
print(DataPullRequestHttpsUpload.to_json())

# convert the object into a dict
data_pull_request_https_upload_dict = data_pull_request_https_upload_instance.to_dict()
# create an instance of DataPullRequestHttpsUpload from a dict
data_pull_request_https_upload_from_dict = DataPullRequestHttpsUpload.from_dict(data_pull_request_https_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


