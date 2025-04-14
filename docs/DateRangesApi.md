# cm_python_openapi_sdk.DateRangesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_date_ranges**](DateRangesApi.md#accept_date_ranges) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/dateRanges | Accept date ranges
[**get_date_ranges**](DateRangesApi.md#get_date_ranges) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/dateRanges/{dwhCacheId} | Get date ranges


# **accept_date_ranges**
> QueriesResponse accept_date_ranges(project_id, dwh_cluster_id, dwh_date_range_request)

Accept date ranges

Accepts a date ranges request. This endpoint returns date ranges for date property in fact table and connected date dimension (if present).

There is one mandatory key `from` that defines the date property in a fact table. Optionally, request can specify `filter` for selecting a date range. In `filter`, it's possible to specify either `function`, or `value` as `startDate` and `endDate`. See the Request body example.

This request starts an asynchronous action, which computes the date ranges result and returns the location URI of the result in the `location` response header. To get the result, client must make another GET request on this URI (see [getDateRanges](#operation/getDateRanges)).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_date_range_request import DwhDateRangeRequest
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
    api_instance = cm_python_openapi_sdk.DateRangesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_date_range_request = cm_python_openapi_sdk.DwhDateRangeRequest() # DwhDateRangeRequest | 

    try:
        # Accept date ranges
        api_response = api_instance.accept_date_ranges(project_id, dwh_cluster_id, dwh_date_range_request)
        print("The response of DateRangesApi->accept_date_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DateRangesApi->accept_date_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_date_range_request** | [**DwhDateRangeRequest**](DwhDateRangeRequest.md)|  | 

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
**202** | Accepted - date range request was successfully accepted for processing |  * location - URI of overlaps result <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_date_ranges**
> DwhDateRangeResponse get_date_ranges(project_id, dwh_cluster_id, dwh_cache_id)

Get date ranges

Get the result of the asynchronous date ranges request submitted in [acceptDateRanges](#operation/acceptDateRanges).
This endpoint implements long polling - see details in [getQueries](#operation/getQueries).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_date_range_response import DwhDateRangeResponse
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
    api_instance = cm_python_openapi_sdk.DateRangesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_cache_id = 'q:vb2b3d8v91jao331:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache

    try:
        # Get date ranges
        api_response = api_instance.get_date_ranges(project_id, dwh_cluster_id, dwh_cache_id)
        print("The response of DateRangesApi->get_date_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DateRangesApi->get_date_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 

### Return type

[**DwhDateRangeResponse**](DwhDateRangeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - date ranges was successfully executed |  -  |
**404** | Not Found - date ranges cache was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

