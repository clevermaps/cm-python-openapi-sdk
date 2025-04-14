# cm_python_openapi_sdk.CachesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cache**](CachesApi.md#get_cache) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/caches/{dwhMaterializedCacheId} | 


# **get_cache**
> get_cache(project_id, dwh_cluster_id, dwh_materialized_cache_id)

Parts of SQL query could be materialized as SQL materialized views and reused during report computations. This resource allow to check if the SQL cache is already materialized and or not.
No cache data is returned.


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
    api_instance = cm_python_openapi_sdk.CachesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_materialized_cache_id = 'if_0xNW_I7qO2A9-1UmZecWvg' # str | Id of the dwh materialized cache

    try:
        api_instance.get_cache(project_id, dwh_cluster_id, dwh_materialized_cache_id)
    except Exception as e:
        print("Exception when calling CachesApi->get_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_materialized_cache_id** | **str**| Id of the dwh materialized cache | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - cache exists |  -  |
**404** | Not Found - cache does not exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

