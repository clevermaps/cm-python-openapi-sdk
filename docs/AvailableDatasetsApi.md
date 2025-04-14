# cm_python_openapi_sdk.AvailableDatasetsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_datasets**](AvailableDatasetsApi.md#available_datasets) | **POST** /projects/{projectId}/dwh/{dwhClusterId}/availableDatasets | 


# **available_datasets**
> AvailableDatasetsResponse available_datasets(project_id, dwh_cluster_id, available_datasets_request, type=type, subtype=subtype, expand=expand, var_from=var_from)

Finds list of datasets available as granularity for given metric(s).

The project's data model defines the relations among datasets. Not all metrics are computable at all datasets granularity. E.g. population defined on state level cannot be calculated for granularity (dataset) city.

This endpoint checks the relations from data model and lists only the available datasets for the metrics.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.available_datasets_request import AvailableDatasetsRequest
from cm_python_openapi_sdk.models.available_datasets_response import AvailableDatasetsResponse
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
    api_instance = cm_python_openapi_sdk.AvailableDatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dwh_cluster_id = 'dwh_cluster_id_example' # str | Id of the dwh cluster
    available_datasets_request = cm_python_openapi_sdk.AvailableDatasetsRequest() # AvailableDatasetsRequest | 
    type = 'dwh' # str | If the parameter present, only the datasets of given type(s) are returned. Parameter can be repeated. (optional)
    subtype = 'geometryPoint' # str | If the parameter present, only the dwh datasets of given subtype(s) are returned. Parameter can be repeated, e.g. `?subtype=geometryLine&subtype=geometryPolygon`  If a parameter `type=dwh` is present then a subtype parameter is ignored and all subtypes of dwh datasets are returned.  (optional)
    expand = 'expand_example' # str | Expand datasets to minimalize roundtrips. (optional)
    var_from = 'clients.postcode_point' # str | Specify the dataset foreign key to limit list of available datasets. This allows to find just datasets from one date dimension. Alterantively, you can specify the model subtree by setting a primary key of dataset. In this case, only the dataset specified by it's primary key and the connected datasets will be returned.  (optional)

    try:
        api_response = api_instance.available_datasets(project_id, dwh_cluster_id, available_datasets_request, type=type, subtype=subtype, expand=expand, var_from=var_from)
        print("The response of AvailableDatasetsApi->available_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailableDatasetsApi->available_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dwh_cluster_id** | **str**| Id of the dwh cluster | 
 **available_datasets_request** | [**AvailableDatasetsRequest**](AvailableDatasetsRequest.md)|  | 
 **type** | **str**| If the parameter present, only the datasets of given type(s) are returned. Parameter can be repeated. | [optional] 
 **subtype** | **str**| If the parameter present, only the dwh datasets of given subtype(s) are returned. Parameter can be repeated, e.g. &#x60;?subtype&#x3D;geometryLine&amp;subtype&#x3D;geometryPolygon&#x60;  If a parameter &#x60;type&#x3D;dwh&#x60; is present then a subtype parameter is ignored and all subtypes of dwh datasets are returned.  | [optional] 
 **expand** | **str**| Expand datasets to minimalize roundtrips. | [optional] 
 **var_from** | **str**| Specify the dataset foreign key to limit list of available datasets. This allows to find just datasets from one date dimension. Alterantively, you can specify the model subtree by setting a primary key of dataset. In this case, only the dataset specified by it&#39;s primary key and the connected datasets will be returned.  | [optional] 

### Return type

[**AvailableDatasetsResponse**](AvailableDatasetsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

