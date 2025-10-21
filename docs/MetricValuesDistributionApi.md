# cm_python_openapi_sdk.MetricValuesDistributionApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_metric_values_distributions**](MetricValuesDistributionApi.md#accept_metric_values_distributions) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/metricValuesDistributions | 
[**get_metric_values_distributions**](MetricValuesDistributionApi.md#get_metric_values_distributions) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/metricValuesDistributions/{dwhCacheId} | 


# **accept_metric_values_distributions**
> QueriesResponse accept_metric_values_distributions(project_id, dwh_cluster_id, dwh_metric_values_distribution_request)

Executes a multidimensional query and returns the data distribution of given metric.

This resource is typically used for the histogram filter distribution.

This request starts an asynchronous action, which computes the metric values distributions result and returns the location URI of the result in `location` response header. To get the result, client must make another GET request on this URI (see [getMetricValuesDistribution](#operation/getMetricValuesDistribution)).

**Distribution methods**

There are currently supported two distribution methods for counting number of elements.
Each method has a custom parameter in request body (see request examples bellow):
- buckets (int) - number of bucket for the dynamic splitting
- breakpoints (array) - array of breakpoints for static segments

**Dynamic buckets split**

Metric range is split into required number of equal size buckets. 
The frequency is the count of occurrences of given metric in these buckets. The range values depends on a granularity - that is defined by query properties.

**Static breakpoints for segments**

Executes a multidimensional query and returns the number of records in each segment. 
Segments are defined as static breakpoints of the metric distribution. 
To the first segment are counted all regions whose value of metric is between <breakpoint[0], breakpoint[1]>. 
The interval for second segment is (breakpoint[1], breakpoint[2]>. And the last segment is (breakpoint[last-1], breakpoint[last]>. 
The minimal required number of breakpoints is 2, it returns count of elements in one segment.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_request import DwhMetricValuesDistributionRequest
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
    api_instance = cm_python_openapi_sdk.MetricValuesDistributionApi(api_client)
    project_id = 'srb6iq85a8h0ors3' # str | Id of the project
    dwh_cluster_id = 'cmstd1' # str | Id of the dwh cluster
    dwh_metric_values_distribution_request = cm_python_openapi_sdk.DwhMetricValuesDistributionRequest() # DwhMetricValuesDistributionRequest | 

    try:
        api_response = api_instance.accept_metric_values_distributions(project_id, dwh_cluster_id, dwh_metric_values_distribution_request)
        print("The response of MetricValuesDistributionApi->accept_metric_values_distributions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricValuesDistributionApi->accept_metric_values_distributions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_metric_values_distribution_request** | [**DwhMetricValuesDistributionRequest**](DwhMetricValuesDistributionRequest.md)|  | 

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

# **get_metric_values_distributions**
> DwhMetricValuesDistributionResponse1 get_metric_values_distributions(project_id, dwh_cluster_id, dwh_cache_id)

Get the result of the asynchronous metric values distributions request submitted in [acceptMetricValuesDistribution](#operation/acceptMetricValuesDistribution).

This endpoint implements long polling - see details in [getQueries](#operation/getQueries).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_response1 import DwhMetricValuesDistributionResponse1
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
    api_instance = cm_python_openapi_sdk.MetricValuesDistributionApi(api_client)
    project_id = 'srb6iq85a8h0ors3' # str | Id of the project
    dwh_cluster_id = 'cmstd1' # str | Id of the dwh cluster
    dwh_cache_id = 'q:f76on62tb6bpitbb:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache

    try:
        api_response = api_instance.get_metric_values_distributions(project_id, dwh_cluster_id, dwh_cache_id)
        print("The response of MetricValuesDistributionApi->get_metric_values_distributions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricValuesDistributionApi->get_metric_values_distributions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 

### Return type

[**DwhMetricValuesDistributionResponse1**](DwhMetricValuesDistributionResponse1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - metric values distributions was successfully executed |  -  |
**404** | Not Found - metric values distributions result was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

