# DataCompleteMultipartUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upload_id** | **str** |  | [optional] 
**part_e_tags** | [**List[PartETag]**](PartETag.md) |  | 

## Example

```python
from cm_python_openapi_sdk.models.data_complete_multipart_upload_request import DataCompleteMultipartUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataCompleteMultipartUploadRequest from a JSON string
data_complete_multipart_upload_request_instance = DataCompleteMultipartUploadRequest.from_json(json)
# print the JSON string representation of the object
print(DataCompleteMultipartUploadRequest.to_json())

# convert the object into a dict
data_complete_multipart_upload_request_dict = data_complete_multipart_upload_request_instance.to_dict()
# create an instance of DataCompleteMultipartUploadRequest from a dict
data_complete_multipart_upload_request_from_dict = DataCompleteMultipartUploadRequest.from_dict(data_complete_multipart_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


