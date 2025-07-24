# cm_python_openapi_sdk.SearchApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**full_text_search**](SearchApi.md#full_text_search) | **GET** /projects/{projectId}/search | Full text search on all internal project data.


# **full_text_search**
> SearchQueryResponse full_text_search(project_id, query, page=page, size=size, dataset=dataset)

Full text search on all internal project data.

Full text search on all internal project data.
The search service indexes title and subtitle of all geometry datasets
(`geometryPoint`, `geometryLine`, `geometryPolygon`).

The dataset is indexed during dataset `pull job`. It means that if the `title` or `subtitle`
definition is changed in dataset's metadata definition, the affected dataset must be fully loaded again.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.search_query_response import SearchQueryResponse
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
    api_instance = cm_python_openapi_sdk.SearchApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    query = 'Birmingham' # str | Query search phrase. It is split into terms and the resource return dataset's object that contains all terms in their `title` or `subtitle`.
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    dataset = 'district' # str | Search only in given dataset. If the parameter present, only the search results of given datasets are returned. Parameter can be repeated, e.g. `&dataset=orders&dataset=customers` (optional)

    try:
        # Full text search on all internal project data.
        api_response = api_instance.full_text_search(project_id, query, page=page, size=size, dataset=dataset)
        print("The response of SearchApi->full_text_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->full_text_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **query** | **str**| Query search phrase. It is split into terms and the resource return dataset&#39;s object that contains all terms in their &#x60;title&#x60; or &#x60;subtitle&#x60;. | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **dataset** | **str**| Search only in given dataset. If the parameter present, only the search results of given datasets are returned. Parameter can be repeated, e.g. &#x60;&amp;dataset&#x3D;orders&amp;dataset&#x3D;customers&#x60; | [optional] 

### Return type

[**SearchQueryResponse**](SearchQueryResponse.md)

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

