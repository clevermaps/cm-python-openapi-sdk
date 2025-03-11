# cm_python_openapi_sdk.DataSourcesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_data_sources**](DataSourcesApi.md#get_all_data_sources) | **GET** /projects/{projectId}/md/dataSources | Return list of all unique data sources specified in datasets of a project


# **get_all_data_sources**
> DataSourcePagedModelDTO get_all_data_sources(project_id, page=page, size=size)

Return list of all unique data sources specified in datasets of a project

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_source_paged_model_dto import DataSourcePagedModelDTO
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
    api_instance = cm_python_openapi_sdk.DataSourcesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)

    try:
        # Return list of all unique data sources specified in datasets of a project
        api_response = api_instance.get_all_data_sources(project_id, page=page, size=size)
        print("The response of DataSourcesApi->get_all_data_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->get_all_data_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]

### Return type

[**DataSourcePagedModelDTO**](DataSourcePagedModelDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

