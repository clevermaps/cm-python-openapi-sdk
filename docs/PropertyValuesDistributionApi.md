# cm_python_openapi_sdk.PropertyValuesDistributionApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_property_values_distribution**](PropertyValuesDistributionApi.md#accept_property_values_distribution) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/propertyValuesDistributions | 
[**get_property_values_distribution**](PropertyValuesDistributionApi.md#get_property_values_distribution) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/propertyValuesDistributions/{dwhCacheId} | 


# **accept_property_values_distribution**
> QueriesResponse accept_property_values_distribution(project_id, dwh_cluster_id, dwh_property_values_distribution_request)

Computes the distribution (frequency) of given fact (numeric dataset property). Result is splitted into required number of equal size buckets. The frequency is the count of occurencies of given metric in these buckets.

This resource is typically used for the histogram filter distribution.

This request starts an asynchronous action, which computes the property values distributions result and returns the location URI of the result in `location` response header. To get the result, client must make another GET request on this URI (see [getPropertyValuesDistribution](#operation/getPropertyValuesDistribution)).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_property_values_distribution_request import DwhPropertyValuesDistributionRequest
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
    api_instance = cm_python_openapi_sdk.PropertyValuesDistributionApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_property_values_distribution_request = cm_python_openapi_sdk.DwhPropertyValuesDistributionRequest() # DwhPropertyValuesDistributionRequest | 

    try:
        api_response = api_instance.accept_property_values_distribution(project_id, dwh_cluster_id, dwh_property_values_distribution_request)
        print("The response of PropertyValuesDistributionApi->accept_property_values_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyValuesDistributionApi->accept_property_values_distribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_property_values_distribution_request** | [**DwhPropertyValuesDistributionRequest**](DwhPropertyValuesDistributionRequest.md)|  | 

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

# **get_property_values_distribution**
> DwhMetricValuesDistributionResponse get_property_values_distribution(project_id, dwh_cluster_id, dwh_cache_id, null_cache_id, var_property)

Get the result of the asynchronous property values distributions request submitted in [acceptPropertyValuesDistribution](#operation/acceptPropertyValuesDistribution).

This endpoint implements long polling - see details in [getQueries](#operation/getQueries).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_metric_values_distribution_response import DwhMetricValuesDistributionResponse
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
    api_instance = cm_python_openapi_sdk.PropertyValuesDistributionApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_cache_id = 'q:vb2b3d8v91jao331:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache
    null_cache_id = 'q:vb2b3d8v91jao331:Ntit7mTcDMxvj7DTI6wuFA' # str | The ID of a cached null values distribution result
    var_property = 'baskets.amount' # str | Dataset's property identifier

    try:
        api_response = api_instance.get_property_values_distribution(project_id, dwh_cluster_id, dwh_cache_id, null_cache_id, var_property)
        print("The response of PropertyValuesDistributionApi->get_property_values_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyValuesDistributionApi->get_property_values_distribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 
 **null_cache_id** | **str**| The ID of a cached null values distribution result | 
 **var_property** | **str**| Dataset&#39;s property identifier | 

### Return type

[**DwhMetricValuesDistributionResponse**](DwhMetricValuesDistributionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - property values distributions was successfully executed |  -  |
**404** | Not Found - property values distributions result was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

