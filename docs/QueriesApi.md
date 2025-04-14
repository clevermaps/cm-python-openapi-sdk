# cm_python_openapi_sdk.QueriesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_queries**](QueriesApi.md#accept_queries) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/queries | Accept queries
[**get_queries**](QueriesApi.md#get_queries) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/queries/{dwhCacheId} | Get queries


# **accept_queries**
> QueriesResponse accept_queries(project_id, dwh_cluster_id, dwh_query_request1, size=size, page=page)

Accept queries

Accepts a query to be computed on a data warehouse. This is the main endpoint for computing data messages on a multidimensional data model.

The POST of an query request starts an asynchronous task and returns the location URI of the result in `location` response header.
To get the status of asynchronous report result computation, client must make another GET request on the URI from `location` header (see [getQueries](#operation/getQueries)).

More information about functions and building CleverMaps metrics is described in the developer documentation:
- [Metric's documentation](https://docs.clevermaps.io/docs/metrics)
- [DWH query function list](https://docs.clevermaps.io/docs/metrics#Metrics-DWHqueryfunctionlistDWH-query-function-list)
- [Filter operators list ](https://docs.clevermaps.io/docs/metrics#Metrics-FilteroperatorslistFilter-operators-list)
- [Metrics cheatsheet](https://docs.clevermaps.io/docs/metrics-cheatsheet)


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_query_request1 import DwhQueryRequest1
from cm_python_openapi_sdk.models.queries_response import QueriesResponse
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
    api_instance = cm_python_openapi_sdk.QueriesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_query_request1 = cm_python_openapi_sdk.DwhQueryRequest1() # DwhQueryRequest1 | 
    size = 200 # int | The count of records to return for one page (optional) (default to 200)
    page = 0 # int | Number of the page (optional) (default to 0)

    try:
        # Accept queries
        api_response = api_instance.accept_queries(project_id, dwh_cluster_id, dwh_query_request1, size=size, page=page)
        print("The response of QueriesApi->accept_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->accept_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_query_request1** | [**DwhQueryRequest1**](DwhQueryRequest1.md)|  | 
 **size** | **int**| The count of records to return for one page | [optional] [default to 200]
 **page** | **int**| Number of the page | [optional] [default to 0]

### Return type

[**QueriesResponse**](QueriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted - query was successfully accepted for processing |  * location - URI of overlaps result <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queries**
> QueryResponse get_queries(project_id, dwh_cluster_id, dwh_cache_id)

Get queries

Get the result of the asynchronous query request submitted in [acceptQueries](#operation/acceptQueries).

This endpoint implements long polling - the client polls the Location URI and the server holds the request open until the query result is available. Then returns either successful or failed response.

It is also possible that the request will time out and respond with 404 after 30s. This can mean two things:
* The result is still being computed
* The result was not found

In that case, the client can make another request and wait if the result will be computed in another 30s interval. The number of repeated GET requests is up to the client.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.query_response import QueryResponse
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
    api_instance = cm_python_openapi_sdk.QueriesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_cache_id = 'q:vb2b3d8v91jao331:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache

    try:
        # Get queries
        api_response = api_instance.get_queries(project_id, dwh_cluster_id, dwh_cache_id)
        print("The response of QueriesApi->get_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->get_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - query was successfully executed |  -  |
**404** | Not Found - the cache was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

