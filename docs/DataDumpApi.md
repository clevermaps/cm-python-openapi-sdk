# cm_python_openapi_sdk.DataDumpApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_dump**](DataDumpApi.md#get_data_dump) | **GET** /projects/{projectId}/data/dumps/{dumpId} | Get data dump file


# **get_data_dump**
> str get_data_dump(project_id, dump_id)

Get data dump file

When the dumpData job is complete, the **dumps** resource returns links for downloading the dumped files.
Dumps are available for the next **24 hours** and then are removed.

### The Output CSV File Format

The output follows the **comma-separated format** as defined by [RFC 4180](https://tools.ietf.org/html/rfc4180) with a header as the first line:

- **HEADER** – The first line contains column headers.
- **DELIMITER `,`** – Cells are separated by a comma.

**Security**
Restricted to LOAD_DATA, DATA_EDITOR and ADMIN project's roles that have permission to load data into the project.


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
    api_instance = cm_python_openapi_sdk.DataDumpApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dump_id = '1fuYh8ApOR1rwu3Zo8xqI0p333jnrLEU' # str | ID of dump returned as result of job

    try:
        # Get data dump file
        api_response = api_instance.get_data_dump(project_id, dump_id)
        print("The response of DataDumpApi->get_data_dump:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataDumpApi->get_data_dump: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dump_id** | **str**| ID of dump returned as result of job | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data dump file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

