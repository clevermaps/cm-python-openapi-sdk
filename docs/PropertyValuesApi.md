# cm_python_openapi_sdk.PropertyValuesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_property_values**](PropertyValuesApi.md#accept_property_values) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/propertyValues | Accept property values
[**get_property_values**](PropertyValuesApi.md#get_property_values) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/propertyValues/{dwhCacheId} | Get property values


# **accept_property_values**
> QueriesResponse accept_property_values(project_id, dwh_cluster_id, dwh_property_values_request, size=size, page=page, sort=sort)

Accept property values

Gets list of distinct values of given dataset's property. The property is set by mandatory request body attribute `property`. The distinct values are returned as pageable response. By default, the values are ordered ascending by the property value. Optionaly the sort order can be changed and the values can be sorted by another propety (eg. sort day of week by day id instead of day name).

This resource is typically used for fetching of the multiSelect and singleSelect filter content.

This request starts an asynchronous action, which computes the property values result and returns the location URI of the result in `location` response header. To get the result, client must make another GET request on this URI (see [getPropertyValues](#operation/getPropertyValues)).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dwh_property_values_request import DwhPropertyValuesRequest
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
    api_instance = cm_python_openapi_sdk.PropertyValuesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_property_values_request = cm_python_openapi_sdk.DwhPropertyValuesRequest() # DwhPropertyValuesRequest | 
    size = 200 # int | The count of records to return for one page (optional) (default to 200)
    page = 0 # int | Number of the page (optional) (default to 0)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Accept property values
        api_response = api_instance.accept_property_values(project_id, dwh_cluster_id, dwh_property_values_request, size=size, page=page, sort=sort)
        print("The response of PropertyValuesApi->accept_property_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyValuesApi->accept_property_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_property_values_request** | [**DwhPropertyValuesRequest**](DwhPropertyValuesRequest.md)|  | 
 **size** | **int**| The count of records to return for one page | [optional] [default to 200]
 **page** | **int**| Number of the page | [optional] [default to 0]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

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

# **get_property_values**
> PropertyValuesResponse get_property_values(project_id, dwh_cluster_id, dwh_cache_id, size=size, page=page)

Get property values

Get the result of the asynchronous property values request submitted in [acceptPropertyValues](#operation/acceptPropertyValues).

This endpoint implements long polling - see details in [getQueries](#operation/getQueries).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.property_values_response import PropertyValuesResponse
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
    api_instance = cm_python_openapi_sdk.PropertyValuesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dwh_cache_id = 'q:vb2b3d8v91jao331:DqBZN5IjSwfufj-7rDMAOQ' # str | Id of the dwh cache
    size = 200 # int | The count of records to return for one page (optional) (default to 200)
    page = 0 # int | Number of the page (optional) (default to 0)

    try:
        # Get property values
        api_response = api_instance.get_property_values(project_id, dwh_cluster_id, dwh_cache_id, size=size, page=page)
        print("The response of PropertyValuesApi->get_property_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyValuesApi->get_property_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dwh_cache_id** | **str**| Id of the dwh cache | 
 **size** | **int**| The count of records to return for one page | [optional] [default to 200]
 **page** | **int**| Number of the page | [optional] [default to 0]

### Return type

[**PropertyValuesResponse**](PropertyValuesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - property values was successfully executed |  -  |
**404** | Not Found - property values result was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

