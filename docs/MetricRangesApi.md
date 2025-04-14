# cm_python_openapi_sdk.MetricRangesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_metric_ranges**](MetricRangesApi.md#accept_metric_ranges) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/metricRanges | Accept metric ranges
[**get_metric_ranges**](MetricRangesApi.md#get_metric_ranges) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/metricRanges/{dwhCacheId} | Get metric ranges


# **accept_metric_ranges**
> QueriesResponse accept_metric_ranges(project_id, dwh_cluster_id, dwh_query_request1)

Accept metric ranges

Accepts a metric ranges request and returns the range values for all given metrics. The range values depend on selected granularity defined in the query properties. Metric Ranges is used for the map legend range.

This request starts an asynchronous action, which computes the metric ranges result and returns the location URI of the result in `location` response header. To get the result, client must make another GET request on this URI (see [getMetricRanges](#operation/getMetricRanges)).


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
    api_instance = cm_python_openapi_sdk.MetricRangesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_query_request1 = cm_python_openapi_sdk.DwhQueryRequest1() # DwhQueryRequest1 | 

    try:
        # Accept metric ranges
        api_response = api_instance.accept_metric_ranges(project_id, dwh_cluster_id, dwh_query_request1)
        print("The response of MetricRangesApi->accept_metric_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricRangesApi->accept_metric_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_query_request1** | [**DwhQueryRequest1**](DwhQueryRequest1.md)|  | 

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
**202** | Accepted - metric ranges query was successfully accepted for processing |  * location - URI of overlaps result <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric_ranges**
> DwhMetricRangeResponse get_metric_ranges(project_id, dwh_cluster_id, dwh_cache_id)

Get metric ranges

Get the result of the asynchronous metric ranges request submitted in [acceptMetricRanges](#operation/acceptMetricRanges).
This endpoint implements long polling - see details in [getQueries](#operation/getQueries).

The resource returns these values for each metric:
* `min` - minimal value for metric in given scope
* `max` - maximal value for metric in given scope


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_metric_range_response import DwhMetricRangeResponse
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
    api_instance = cm_python_openapi_sdk.MetricRangesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_cache_id = 'q:vb2b3d8v91jao331:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache

    try:
        # Get metric ranges
        api_response = api_instance.get_metric_ranges(project_id, dwh_cluster_id, dwh_cache_id)
        print("The response of MetricRangesApi->get_metric_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricRangesApi->get_metric_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 

### Return type

[**DwhMetricRangeResponse**](DwhMetricRangeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - metric ranges request was successfully executed |  -  |
**404** | Not Found - metric ranges result was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

