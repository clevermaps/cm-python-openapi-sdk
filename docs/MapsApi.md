# cm_python_openapi_sdk.MapsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_map**](MapsApi.md#create_map) | **POST** /projects/{projectId}/md/maps | Creates new Map.
[**delete_map_by_id**](MapsApi.md#delete_map_by_id) | **DELETE** /projects/{projectId}/md/maps/{id} | Deletes map by id
[**get_all_maps**](MapsApi.md#get_all_maps) | **GET** /projects/{projectId}/md/maps | Returns paged collection of all Maps in a project.
[**get_map_by_id**](MapsApi.md#get_map_by_id) | **GET** /projects/{projectId}/md/maps/{id} | Gets map by id
[**update_map_by_id**](MapsApi.md#update_map_by_id) | **PUT** /projects/{projectId}/md/maps/{id} | Updates map by id


# **create_map**
> MapDTO create_map(project_id, map_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new Map.

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.map_dto import MapDTO
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
    api_instance = cm_python_openapi_sdk.MapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    map_dto = cm_python_openapi_sdk.MapDTO() # MapDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new Map.
        api_response = api_instance.create_map(project_id, map_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of MapsApi->create_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->create_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **map_dto** | [**MapDTO**](MapDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**MapDTO**](MapDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Map with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_map_by_id**
> delete_map_by_id(project_id, id)

Deletes map by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

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
    api_instance = cm_python_openapi_sdk.MapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the map

    try:
        # Deletes map by id
        api_instance.delete_map_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling MapsApi->delete_map_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the map | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Map was successfully deleted |  -  |
**404** | Map not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_maps**
> MapPagedModelDTO get_all_maps(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Maps in a project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.map_paged_model_dto import MapPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.MapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Maps in a project.
        api_response = api_instance.get_all_maps(project_id, page=page, size=size, sort=sort)
        print("The response of MapsApi->get_all_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_all_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**MapPagedModelDTO**](MapPagedModelDTO.md)

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

# **get_map_by_id**
> MapDTO get_map_by_id(project_id, id)

Gets map by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.map_dto import MapDTO
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
    api_instance = cm_python_openapi_sdk.MapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the map

    try:
        # Gets map by id
        api_response = api_instance.get_map_by_id(project_id, id)
        print("The response of MapsApi->get_map_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_map_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the map | 

### Return type

[**MapDTO**](MapDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Map not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_map_by_id**
> MapDTO update_map_by_id(project_id, id, if_match, map_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates map by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.map_dto import MapDTO
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
    api_instance = cm_python_openapi_sdk.MapsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the map
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    map_dto = cm_python_openapi_sdk.MapDTO() # MapDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates map by id
        api_response = api_instance.update_map_by_id(project_id, id, if_match, map_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of MapsApi->update_map_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->update_map_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the map | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **map_dto** | [**MapDTO**](MapDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**MapDTO**](MapDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Map not found |  -  |
**409** | Map with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

