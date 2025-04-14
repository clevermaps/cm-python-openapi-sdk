# cm_python_openapi_sdk.OverlapsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_overlaps**](OverlapsApi.md#accept_overlaps) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/overlaps | Accept overlaps
[**get_overlaps**](OverlapsApi.md#get_overlaps) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/overlaps/{dwhCacheId} | Get overlaps


# **accept_overlaps**
> QueriesResponse accept_overlaps(project_id, dwh_cluster_id, dwh_overlaps_request)

Accept overlaps

Computes set of operations between two objects for given metric on selected granularity level. The result is the metric value for the areas.

Supported operations:
  * `subtract` - metric value for areas exclusively covered by one object (areas covered by objectA subtract areas covered by objectB)
  * `intersect` - metric value for areas covered by both objects (areas covered by objectA and by objectB)
  * `major_dominance` - metric value for areas where an object has a major dominance (a value of it's metric is more than 90% in compare with the other object)
  * `minor_dominance` - metric value for areas where an object has minor dominance (a value of it's metric is less than 90% but more than 60% in compare with the other object)
  * `equivalent_dominance` - metric value for areas where both objects have a similar share (a ratio of metric's values is between 40 - 60%)

This request starts an asynchronous action, which computes the overlaps result and returns the location URI of the result in `location` response header. To get the result, client must make another GET request on this URI (see [getOverlaps](#operation/getOverlaps)).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_overlaps_request import DwhOverlapsRequest
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
    api_instance = cm_python_openapi_sdk.OverlapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_overlaps_request = cm_python_openapi_sdk.DwhOverlapsRequest() # DwhOverlapsRequest | 

    try:
        # Accept overlaps
        api_response = api_instance.accept_overlaps(project_id, dwh_cluster_id, dwh_overlaps_request)
        print("The response of OverlapsApi->accept_overlaps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverlapsApi->accept_overlaps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_overlaps_request** | [**DwhOverlapsRequest**](DwhOverlapsRequest.md)|  | 

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
**202** | Accepted - request was accepted for processing |  * location - URI of overlaps result <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overlaps**
> DwhOverlapsResponse get_overlaps(project_id, dwh_cluster_id, dwh_cache_id)

Get overlaps

Get the result of the asynchronous overlaps request submitted in [acceptOverlaps](#operation/acceptOverlaps).

This endpoint implements long polling - see details in [getQueries](#operation/getQueries).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_overlaps_response import DwhOverlapsResponse
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
    api_instance = cm_python_openapi_sdk.OverlapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_cache_id = 'q:vb2b3d8v91jao331:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache

    try:
        # Get overlaps
        api_response = api_instance.get_overlaps(project_id, dwh_cluster_id, dwh_cache_id)
        print("The response of OverlapsApi->get_overlaps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OverlapsApi->get_overlaps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 

### Return type

[**DwhOverlapsResponse**](DwhOverlapsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - overlaps request was successfully executed |  -  |
**404** | Not Found - overlaps result was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

