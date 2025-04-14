# DataUpload200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upload_url** | **str** |  | 
**upload_url_encoded** | **str** |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 
**upload_id** | **str** |  | 
**upload_urls** | **List[str]** |  | 
**upload_urls_encoded** | **List[str]** |  | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_upload200_response import DataUpload200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DataUpload200Response from a JSON string
data_upload200_response_instance = DataUpload200Response.from_json(json)
# print the JSON string representation of the object
print(DataUpload200Response.to_json())

# convert the object into a dict
data_upload200_response_dict = data_upload200_response_instance.to_dict()
# create an instance of DataUpload200Response from a dict
data_upload200_response_from_dict = DataUpload200Response.from_dict(data_upload200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


