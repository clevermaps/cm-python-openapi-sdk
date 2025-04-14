# cm_python_openapi_sdk.ExplainApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explain**](ExplainApi.md#explain) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/explain | Explain query


# **explain**
> str explain(project_id, dwh_cluster_id, page=page, size=size)

Explain query

This resource is useful for debugging and tuning DWH queries. The resource accepts standard DWH Queries (see [acceptQueries](#operation/acceptQueries))and shows the corresponding SQL statement.)


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
    api_instance = cm_python_openapi_sdk.ExplainApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)

    try:
        # Explain query
        api_response = api_instance.explain(project_id, dwh_cluster_id, page=page, size=size)
        print("The response of ExplainApi->explain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplainApi->explain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - query explain was successfully prepared |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

