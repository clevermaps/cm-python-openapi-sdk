# cm_python_openapi_sdk.GeosearchApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geographic_search**](GeosearchApi.md#geographic_search) | **GET** /geosearch | Geographic search


# **geographic_search**
> GeosearchPagedModelDTO geographic_search(query, page=page, size=size, country=country, language=language, types=types)

Geographic search

Wrapper of [Mapbox Geocoding service](https://docs.mapbox.com/api/search/geocoding/). Processes the query and validates the URL parameters. If the query is valid, it is executed on Mapbox API. The result is then translated and returned.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.geosearch_paged_model_dto import GeosearchPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.GeosearchApi(api_client)
    query = 'Birmingham' # str | Query search phrase. It is highlighted in the query result.
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    country = 'GB' # str | Array of ISO 3166 alpha-2 country codes to limit the search. (optional)
    language = 'en' # str | Language to use for query results as defined by ISO 639-1. (optional)
    types = 'city, locality, address' # str | Array of place types, available types are [region, district, city, locality, address, postcode] (optional)

    try:
        # Geographic search
        api_response = api_instance.geographic_search(query, page=page, size=size, country=country, language=language, types=types)
        print("The response of GeosearchApi->geographic_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeosearchApi->geographic_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query search phrase. It is highlighted in the query result. | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **country** | **str**| Array of ISO 3166 alpha-2 country codes to limit the search. | [optional] 
 **language** | **str**| Language to use for query results as defined by ISO 639-1. | [optional] 
 **types** | **str**| Array of place types, available types are [region, district, city, locality, address, postcode] | [optional] 

### Return type

[**GeosearchPagedModelDTO**](GeosearchPagedModelDTO.md)

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

