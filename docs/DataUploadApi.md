# cm_python_openapi_sdk.DataUploadApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_multipart_upload**](DataUploadApi.md#complete_multipart_upload) | **PUT** /projects/{projectId}/dwh/data/uploads/{id} | Complete multipart upload
[**data_upload**](DataUploadApi.md#data_upload) | **POST** /projects/{projectId}/dwh/data/uploads | Upload CSV file to dataset


# **complete_multipart_upload**
> DataCompleteMultipartUploadResponse complete_multipart_upload(project_id, id, data_complete_multipart_upload_request)

Complete multipart upload

This resource allows you to complete the multipart upload after all parts are uploaded.
The request body contains the id received in the previous request (e.g. nogeLAvMPlITfWC66ztEDOW6Vl3bwRrn), the uploadId and a list of ETags for each part.
ETag for each part can be found in the ETag response header from the PUT request to part upload.

**Security**
Restricted to LOAD_DATA, DATA_EDITOR and ADMIN project's roles that have permission to load data into the project.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_complete_multipart_upload_request import DataCompleteMultipartUploadRequest
from cm_python_openapi_sdk.models.data_complete_multipart_upload_response import DataCompleteMultipartUploadResponse
from cm_python_openapi_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = cm_python_openapi_sdk.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = cm_python_openapi_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cm_python_openapi_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cm_python_openapi_sdk.DataUploadApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'nogeLAvMPlITfWC66ztEDOW6Vl3bwRrn' # str | 
    data_complete_multipart_upload_request = cm_python_openapi_sdk.DataCompleteMultipartUploadRequest() # DataCompleteMultipartUploadRequest | 

    try:
        # Complete multipart upload
        api_response = api_instance.complete_multipart_upload(project_id, id, data_complete_multipart_upload_request)
        print("The response of DataUploadApi->complete_multipart_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataUploadApi->complete_multipart_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**|  | 
 **data_complete_multipart_upload_request** | [**DataCompleteMultipartUploadRequest**](DataCompleteMultipartUploadRequest.md)|  | 

### Return type

[**DataCompleteMultipartUploadResponse**](DataCompleteMultipartUploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful completion of uploading data to S3 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_upload**
> DataUpload200Response data_upload(project_id, parts=parts)

Upload CSV file to dataset

# Data Upload Methods

There are four ways to update dataset data:

  1. **CSV Upload** – Push a CSV file from your computer or server.
  2. **Multipart CSV Upload** – Push CSV file in parts from your computer or server (recommended for files larger then 50MB)
    - you must specify parameter **parts**
  3. **S3 Pull** – Pull data stored in your S3 bucket.
  4. **HTTPS Pull** – Pull data from any HTTPS endpoint.

---

## CSV Upload Flow

1. Create a new upload resource via: `POST /rest/projects/{projectId}/dwh/data/uploads`
2. Receive a resource with an S3 pre-signed `uploadUrl`.
3. Upload the CSV file using: `PUT {uploadUrl}` (No authentication required)
4. Once the upload is finished, start a [dataPull](#operation/submitJobExecution) job with the correct input.

### Pre-signed URL Usage
The pre-signed URL can be used with any HTTP tool. You can upload the content directly without additional authorization (no bearer token required).

#### Example: Upload CSV File Using `curl`
```sh
curl -X PUT \
'https://s3-eu-west-1.amazonaws.com/can-dwh-upload-uploads-prod/00ubftx6v6TSTKnAt0h7/o3d2ov0p43msl3hf/RjFJt5kW302QNLzFIVnxN369dlY6KUw4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJ6BXDNGJ7WFCT7SQ%2F20170915%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20170915T141016Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e053197d044345041268b7f22918e2e71e2a3d5a23ceed65a332e1782998739c' \
-T /home/user/data/mydata.csv
```
## Multipart Upload Flow

To upload a large CSV file in multiple parts, follow these steps:

1. **Start the multipart upload** by sending a `POST` request: POST /rest/projects/{projectId}/dwh/data/uploads?parts=3
  - This request initializes the upload and specifies the number of parts.
2. **Receive a response** containing:
  - An `id` identifying the upload.
  - A list of **uploadUrls**, which are S3 pre-signed URLs, one for each part.
3. **Split the CSV file** and upload each part to its corresponding URL using: PUT {uploadUrl}
  - No additional authentication is required.
4. **Complete the upload**
  - Once all parts are uploaded, send the [Complete Multipart Data Upload](#operation/completeMultipartUpload) request.
5. **Start the DataPull job**
  - After completing the upload, start a [dataPull](#operation/submitJobExecution) job with the correct input.

## S3 Pull Flow

Start a [dataPull](#operation/submitJobExecution) job using an **S3 URL**.

### Example: DataPull Request for S3 Upload
```json
{
  "type": "dataPull",
  "projectId": "ncesksvg7rjeri7v",
  "content": {
    "dataset": "mystores",
    "mode": "full",
    "s3Upload": {
      "uri": "s3://can-s3-dwh-pull-test/mystores.csv",
      "accessKeyId": "myAccessKey",
      "secretAccessKey": "mySecretAccessKey"
    },
    "type": "csv"
  }
}
```
## HTTPS Pull Flow

Start a [dataPull](#operation/submitJobExecution) job using an **HTTPS URL**.

### Example: DataPull Request for HTTPS Upload
```json
{
  "type": "dataPull",
  "projectId": "ncesksvg7rjeri7v",
  "content": {
    "dataset": "mystores",
    "mode": "full",
    "httpsUpload": "https://my-domain.com/mystores.csv",
    "type": "csv"
  }
}
```
**Warning**: We do not recommend uploading sensitive information using the HTTPS pull flow,
as files hosted on public URLs are accessible to anyone on the internet.

**Security**
Restricted to LOAD_DATA, DATA_EDITOR and ADMIN project's roles that have permission to load data into the project.

## CSV Options

With **CsvOptions**, you can specify how the CSV should be processed. The available options are:

| Option       | Type      | Description                                                   | Default Value |
|-------------|----------|---------------------------------------------------------------|--------------|
| `header`    | boolean  | Specifies if the CSV has a header.                           | `true`       |
| `separator` | char     | Specifies the separator character between fields.           | `,`          |
| `quote`     | char     | Specifies the quote character.                              | `"`          |
| `escape`    | char     | Specifies the escape character.                             | `\`          |
| `null`      | string   | Specifies the replacement value for custom CSV nulls.      | *None*       |
| `forceNull` | string[] | Specifies which CSV columns should enforce null replacement. | *None*       |

### Example: DataPull Request for S3 Upload with CSV Options
```json
{
  "type": "dataPull",
  "projectId": "ncesksvg7rjeri7v",
  "content": {
    "dataset": "mystores",
    "mode": "full",
    "s3Upload": {
      "uri": "s3://can-s3-dwh-pull-test/mystores.csv",
      "accessKeyId": "myAccessKey",
      "secretAccessKey": "mySecretAccessKey"
    },
    "type": "csv",
    "csvOptions": {
      "header": true,
      "separator": ";",
      "quote": "§",
      "escape": "\\",
      "null": "NULL_VALUE",
      "forceNull": [
        "columnName",
        "otherColumn"
      ]
    }
  }
}
```


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_upload200_response import DataUpload200Response
from cm_python_openapi_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = cm_python_openapi_sdk.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = cm_python_openapi_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cm_python_openapi_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cm_python_openapi_sdk.DataUploadApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    parts = 56 # int |  (optional)

    try:
        # Upload CSV file to dataset
        api_response = api_instance.data_upload(project_id, parts=parts)
        print("The response of DataUploadApi->data_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataUploadApi->data_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **parts** | **int**|  | [optional] 

### Return type

[**DataUpload200Response**](DataUpload200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Links to upload your data to |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

