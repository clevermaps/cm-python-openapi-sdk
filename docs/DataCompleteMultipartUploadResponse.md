# DataCompleteMultipartUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**e_tag** | **str** |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_complete_multipart_upload_response import DataCompleteMultipartUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataCompleteMultipartUploadResponse from a JSON string
data_complete_multipart_upload_response_instance = DataCompleteMultipartUploadResponse.from_json(json)
# print the JSON string representation of the object
print(DataCompleteMultipartUploadResponse.to_json())

# convert the object into a dict
data_complete_multipart_upload_response_dict = data_complete_multipart_upload_response_instance.to_dict()
# create an instance of DataCompleteMultipartUploadResponse from a dict
data_complete_multipart_upload_response_from_dict = DataCompleteMultipartUploadResponse.from_dict(data_complete_multipart_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


