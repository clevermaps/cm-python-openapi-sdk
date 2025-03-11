# cm_python_openapi_sdk.ExportsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_export**](ExportsApi.md#create_export) | **POST** /projects/{projectId}/md/exports | Creates new export
[**delete_export_by_id**](ExportsApi.md#delete_export_by_id) | **DELETE** /projects/{projectId}/md/exports/{id} | Deletes export by id
[**get_all_exports**](ExportsApi.md#get_all_exports) | **GET** /projects/{projectId}/md/exports | Returns paged collection of all Exports in a project
[**get_export_by_id**](ExportsApi.md#get_export_by_id) | **GET** /projects/{projectId}/md/exports/{id} | Gets export by id
[**update_export_by_id**](ExportsApi.md#update_export_by_id) | **PUT** /projects/{projectId}/md/exports/{id} | Updates export by id


# **create_export**
> ExportDTO create_export(project_id, export_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new export

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.export_dto import ExportDTO
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
    api_instance = cm_python_openapi_sdk.ExportsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    export_dto = cm_python_openapi_sdk.ExportDTO() # ExportDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new export
        api_response = api_instance.create_export(project_id, export_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of ExportsApi->create_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->create_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **export_dto** | [**ExportDTO**](ExportDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**ExportDTO**](ExportDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Export with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_export_by_id**
> delete_export_by_id(project_id, id)

Deletes export by id

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
    api_instance = cm_python_openapi_sdk.ExportsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the export

    try:
        # Deletes export by id
        api_instance.delete_export_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling ExportsApi->delete_export_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the export | 

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
**204** | Export was successfully deleted |  -  |
**404** | Export not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_exports**
> ExportPagedModelDTO get_all_exports(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Exports in a project

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.export_paged_model_dto import ExportPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.ExportsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Exports in a project
        api_response = api_instance.get_all_exports(project_id, page=page, size=size, sort=sort)
        print("The response of ExportsApi->get_all_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->get_all_exports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**ExportPagedModelDTO**](ExportPagedModelDTO.md)

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

# **get_export_by_id**
> ExportDTO get_export_by_id(project_id, id)

Gets export by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.export_dto import ExportDTO
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
    api_instance = cm_python_openapi_sdk.ExportsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the export

    try:
        # Gets export by id
        api_response = api_instance.get_export_by_id(project_id, id)
        print("The response of ExportsApi->get_export_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->get_export_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the export | 

### Return type

[**ExportDTO**](ExportDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Export not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_export_by_id**
> ExportDTO update_export_by_id(project_id, id, if_match, export_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates export by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.export_dto import ExportDTO
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
    api_instance = cm_python_openapi_sdk.ExportsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the export
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    export_dto = cm_python_openapi_sdk.ExportDTO() # ExportDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates export by id
        api_response = api_instance.update_export_by_id(project_id, id, if_match, export_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of ExportsApi->update_export_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->update_export_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the export | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **export_dto** | [**ExportDTO**](ExportDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**ExportDTO**](ExportDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Export not found |  -  |
**409** | Export with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

