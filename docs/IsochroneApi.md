# cm_python_openapi_sdk.IsochroneApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_isochrone**](IsochroneApi.md#get_isochrone) | **GET** /isochrone | Get isochrone


# **get_isochrone**
> IsochronePagedModelDTO get_isochrone(lat, lng, profile, unit, amount, size=size, page=page)

Get isochrone

Calculates a list of isochrones for the given point(s).
An **isochrone** is a line that connects points of equal travel time around a given location.
It can be calculated as:

- **Travel Time-Based Isochrone**: Represents the area reachable within a specified amount of time.
  Supported for the following travel modes:
  - `car`
  - `bike`
  - `foot`

- **Distance-Based Isochrone**: Represents a circular area defined by a specified distance (in meters) from a point.
  Supported for the `air` travel mode.

Endpoint accepts multiple points split by comma. For each point you must also define profile, unit and amount, split by comma.
E.g. for two points - profile=foot,car unit=time,time amount=5.20


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.isochrone_paged_model_dto import IsochronePagedModelDTO
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
    api_instance = cm_python_openapi_sdk.IsochroneApi(api_client)
    lat = '49.198004,48.234569' # str | Latitude of the isochrone starting location. Accepts multiple values split by comma.
    lng = '19.698104,18.357981' # str | Longitude of the isochrone starting location. Accepts multiple values split by comma.
    profile = 'car,foot' # str | Profiles of the isochrone, available types: car, bike, foot, air. Accepts multiple values split by comma.
    unit = 'time,time' # str | Unit of the isochrone result, available types: time (for car, bike and foot profiles) or distance (for air profile). Accepts multiple values split by comma.
    amount = '5,20' # str | The amount of either time (minutes for car, bike and foot profiles) or distance (meters for air profile). Accepts multiple values split by comma.
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    page = 0 # int | Number of the page (optional) (default to 0)

    try:
        # Get isochrone
        api_response = api_instance.get_isochrone(lat, lng, profile, unit, amount, size=size, page=page)
        print("The response of IsochroneApi->get_isochrone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsochroneApi->get_isochrone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **str**| Latitude of the isochrone starting location. Accepts multiple values split by comma. | 
 **lng** | **str**| Longitude of the isochrone starting location. Accepts multiple values split by comma. | 
 **profile** | **str**| Profiles of the isochrone, available types: car, bike, foot, air. Accepts multiple values split by comma. | 
 **unit** | **str**| Unit of the isochrone result, available types: time (for car, bike and foot profiles) or distance (for air profile). Accepts multiple values split by comma. | 
 **amount** | **str**| The amount of either time (minutes for car, bike and foot profiles) or distance (meters for air profile). Accepts multiple values split by comma. | 
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **page** | **int**| Number of the page | [optional] [default to 0]

### Return type

[**IsochronePagedModelDTO**](IsochronePagedModelDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged isochrones for given points |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

