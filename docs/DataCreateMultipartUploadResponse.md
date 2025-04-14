# DataCreateMultipartUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upload_id** | **str** |  | 
**upload_urls** | **List[str]** |  | 
**upload_urls_encoded** | **List[str]** |  | [optional] 
**links** | **List[object]** | define keys links and page that are mandatory for all pageble responses | [optional] 

## Example

```python
from cm_python_openapi_sdk.models.data_create_multipart_upload_response import DataCreateMultipartUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataCreateMultipartUploadResponse from a JSON string
data_create_multipart_upload_response_instance = DataCreateMultipartUploadResponse.from_json(json)
# print the JSON string representation of the object
print(DataCreateMultipartUploadResponse.to_json())

# convert the object into a dict
data_create_multipart_upload_response_dict = data_create_multipart_upload_response_instance.to_dict()
# create an instance of DataCreateMultipartUploadResponse from a dict
data_create_multipart_upload_response_from_dict = DataCreateMultipartUploadResponse.from_dict(data_create_multipart_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


