# cm_python_openapi_sdk.VectorTilesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vector_tile**](VectorTilesApi.md#get_vector_tile) | **GET** /projects/{projectId}/dwh/{dwhClusterId}/tiles/{datasetName}/{z}/{x}/{y}.vector.pbf | 


# **get_vector_tile**
> bytearray get_vector_tile(project_id, dwh_cluster_id, dataset_name, z, x, y)

Get a vector tile from a geometryPolygon or geometryLine dataset.
This endpoint provides on-the-fly rendering of vector tiles from DWH geometryLine or geometryPolygon datasets that include a geometry property.

Vector tiles are rendered upon request and cached in a Redis in-memory database to improve performance. Geometries are not generalized, so this endpoint is not optimized for serving very large datasets.

This endpoint synchronously starts the vector tile computation and waits for the data. For very large datasets, the request may time out.
If the vector tile is empty, a 404 response is returned.


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
    api_instance = cm_python_openapi_sdk.VectorTilesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    dataset_name = 'dataset_name_example' # str | Name of the DWH dataset with geometry data
    z = 56 # int | Z coordinate of a vector tile
    x = 56 # int | X coordinate of a vector tile
    y = 56 # int | Y coordinate of a vector tile

    try:
        api_response = api_instance.get_vector_tile(project_id, dwh_cluster_id, dataset_name, z, x, y)
        print("The response of VectorTilesApi->get_vector_tile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorTilesApi->get_vector_tile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **dataset_name** | **str**| Name of the DWH dataset with geometry data | 
 **z** | **int**| Z coordinate of a vector tile | 
 **x** | **int**| X coordinate of a vector tile | 
 **y** | **int**| Y coordinate of a vector tile | 

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mapbox-vector-tile

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - vector tile was successfully processed |  -  |
**400** | Bad Request - dataset is not type geometryPolygon, geometryLine or doesn&#39;t contain geometry data |  -  |
**404** | Not Found - some uri parameter was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

