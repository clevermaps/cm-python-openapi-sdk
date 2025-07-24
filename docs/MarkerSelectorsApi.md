# cm_python_openapi_sdk.MarkerSelectorsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marker_selector**](MarkerSelectorsApi.md#create_marker_selector) | **POST** /projects/{projectId}/md/markerSelectors | Creates new Marker Selector.
[**delete_marker_selector_by_id**](MarkerSelectorsApi.md#delete_marker_selector_by_id) | **DELETE** /projects/{projectId}/md/markerSelectors/{id} | Deletes marker selector by id
[**get_all_marker_selectors**](MarkerSelectorsApi.md#get_all_marker_selectors) | **GET** /projects/{projectId}/md/markerSelectors | Returns paged collection of all Marker Selectors in a project.
[**get_marker_selector_by_id**](MarkerSelectorsApi.md#get_marker_selector_by_id) | **GET** /projects/{projectId}/md/markerSelectors/{id} | Gets marker selector by id
[**get_marker_selector_by_name**](MarkerSelectorsApi.md#get_marker_selector_by_name) | **GET** /projects/{projectId}/md/markerSelectors/{name} | Gets marker selector by name
[**update_marker_selector_by_id**](MarkerSelectorsApi.md#update_marker_selector_by_id) | **PUT** /projects/{projectId}/md/markerSelectors/{id} | Updates marker selector by id


# **create_marker_selector**
> MarkerSelectorResponseDTO create_marker_selector(project_id, marker_selector_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new Marker Selector.

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.marker_selector_dto import MarkerSelectorDTO
from cm_python_openapi_sdk.models.marker_selector_response_dto import MarkerSelectorResponseDTO
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
    api_instance = cm_python_openapi_sdk.MarkerSelectorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    marker_selector_dto = cm_python_openapi_sdk.MarkerSelectorDTO() # MarkerSelectorDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new Marker Selector.
        api_response = api_instance.create_marker_selector(project_id, marker_selector_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of MarkerSelectorsApi->create_marker_selector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerSelectorsApi->create_marker_selector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **marker_selector_dto** | [**MarkerSelectorDTO**](MarkerSelectorDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**MarkerSelectorResponseDTO**](MarkerSelectorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marker selector was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Marker selector with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_marker_selector_by_id**
> delete_marker_selector_by_id(project_id, id)

Deletes marker selector by id

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
    api_instance = cm_python_openapi_sdk.MarkerSelectorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the marker selector

    try:
        # Deletes marker selector by id
        api_instance.delete_marker_selector_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling MarkerSelectorsApi->delete_marker_selector_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the marker selector | 

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
**204** | Marker selector was successfully deleted |  -  |
**404** | Marker selector not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_marker_selectors**
> MarkerSelectorPagedModelDTO get_all_marker_selectors(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Marker Selectors in a project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.marker_selector_paged_model_dto import MarkerSelectorPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.MarkerSelectorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Marker Selectors in a project.
        api_response = api_instance.get_all_marker_selectors(project_id, page=page, size=size, sort=sort)
        print("The response of MarkerSelectorsApi->get_all_marker_selectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerSelectorsApi->get_all_marker_selectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**MarkerSelectorPagedModelDTO**](MarkerSelectorPagedModelDTO.md)

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

# **get_marker_selector_by_id**
> MarkerSelectorResponseDTO get_marker_selector_by_id(project_id, id)

Gets marker selector by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.marker_selector_response_dto import MarkerSelectorResponseDTO
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
    api_instance = cm_python_openapi_sdk.MarkerSelectorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the marker selector

    try:
        # Gets marker selector by id
        api_response = api_instance.get_marker_selector_by_id(project_id, id)
        print("The response of MarkerSelectorsApi->get_marker_selector_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerSelectorsApi->get_marker_selector_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the marker selector | 

### Return type

[**MarkerSelectorResponseDTO**](MarkerSelectorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Marker selector not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marker_selector_by_name**
> MarkerSelectorResponseDTO get_marker_selector_by_name(project_id, name)

Gets marker selector by name

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.marker_selector_response_dto import MarkerSelectorResponseDTO
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
    api_instance = cm_python_openapi_sdk.MarkerSelectorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'name_example' # str | Name of the marker selector

    try:
        # Gets marker selector by name
        api_response = api_instance.get_marker_selector_by_name(project_id, name)
        print("The response of MarkerSelectorsApi->get_marker_selector_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerSelectorsApi->get_marker_selector_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the marker selector | 

### Return type

[**MarkerSelectorResponseDTO**](MarkerSelectorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Marker selector not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_marker_selector_by_id**
> MarkerSelectorResponseDTO update_marker_selector_by_id(project_id, id, if_match, marker_selector_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates marker selector by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.marker_selector_dto import MarkerSelectorDTO
from cm_python_openapi_sdk.models.marker_selector_response_dto import MarkerSelectorResponseDTO
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
    api_instance = cm_python_openapi_sdk.MarkerSelectorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the marker selector
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    marker_selector_dto = cm_python_openapi_sdk.MarkerSelectorDTO() # MarkerSelectorDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates marker selector by id
        api_response = api_instance.update_marker_selector_by_id(project_id, id, if_match, marker_selector_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of MarkerSelectorsApi->update_marker_selector_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerSelectorsApi->update_marker_selector_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the marker selector | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **marker_selector_dto** | [**MarkerSelectorDTO**](MarkerSelectorDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**MarkerSelectorResponseDTO**](MarkerSelectorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marker selector was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Marker selector not found |  -  |
**409** | Marker selector with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

