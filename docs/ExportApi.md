# cm_python_openapi_sdk.ExportApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exported_data**](ExportApi.md#get_exported_data) | **GET** /projects/{projectId}/export/{exportId} | Get exported data


# **get_exported_data**
> str get_exported_data(project_id, export_id)

Get exported data

Get exported data file from S3. Data can be exported by submitting an `export` job to the `/rest/jobs` endpoint.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
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
    api_instance = cm_python_openapi_sdk.ExportApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    export_id = '1fuYh8ApOR1rwu3Zo8xqI0p333jnrLEU' # str | ID of export returned as result of job

    try:
        # Get exported data
        api_response = api_instance.get_exported_data(project_id, export_id)
        print("The response of ExportApi->get_exported_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->get_exported_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **export_id** | **str**| ID of export returned as result of job | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export data file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

