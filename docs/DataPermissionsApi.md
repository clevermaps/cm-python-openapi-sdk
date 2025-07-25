# cm_python_openapi_sdk.DataPermissionsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_permission**](DataPermissionsApi.md#create_data_permission) | **POST** /projects/{projectId}/md/dataPermissions | Creates new data permission
[**delete_data_permission_by_id**](DataPermissionsApi.md#delete_data_permission_by_id) | **DELETE** /projects/{projectId}/md/dataPermissions/{id} | Deletes data permission by id
[**get_all_data_permissions**](DataPermissionsApi.md#get_all_data_permissions) | **GET** /projects/{projectId}/md/dataPermissions | Returns paged collection of all data permissions in a project
[**get_data_permission_by_id**](DataPermissionsApi.md#get_data_permission_by_id) | **GET** /projects/{projectId}/md/dataPermissions/{id} | Gets data permission by id
[**get_data_permission_by_name**](DataPermissionsApi.md#get_data_permission_by_name) | **GET** /projects/{projectId}/md/dataPermissions/{name} | Gets data permission by name
[**update_data_permission_by_id**](DataPermissionsApi.md#update_data_permission_by_id) | **PUT** /projects/{projectId}/md/dataPermissions/{id} | Updates data permission by id


# **create_data_permission**
> DataPermissionResponseDTO create_data_permission(project_id, data_permission_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new data permission

Restricted to ADMIN project role that has the permission to update data permissions of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_permission_dto import DataPermissionDTO
from cm_python_openapi_sdk.models.data_permission_response_dto import DataPermissionResponseDTO
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
    api_instance = cm_python_openapi_sdk.DataPermissionsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    data_permission_dto = cm_python_openapi_sdk.DataPermissionDTO() # DataPermissionDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new data permission
        api_response = api_instance.create_data_permission(project_id, data_permission_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of DataPermissionsApi->create_data_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataPermissionsApi->create_data_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **data_permission_dto** | [**DataPermissionDTO**](DataPermissionDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**DataPermissionResponseDTO**](DataPermissionResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data permission was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Data permission with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_permission_by_id**
> delete_data_permission_by_id(project_id, id)

Deletes data permission by id

Restricted to ADMIN project role that has the permission to update data permissions of the project.

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
    api_instance = cm_python_openapi_sdk.DataPermissionsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the data permission

    try:
        # Deletes data permission by id
        api_instance.delete_data_permission_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling DataPermissionsApi->delete_data_permission_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the data permission | 

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
**204** | Data permission was successfully deleted |  -  |
**404** | Data permission not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_data_permissions**
> DataPermissionPagedModelDTO get_all_data_permissions(project_id, page=page, size=size, sort=sort)

Returns paged collection of all data permissions in a project

Restricted to ADMIN project role that has the permission to update data permissions of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_permission_paged_model_dto import DataPermissionPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.DataPermissionsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all data permissions in a project
        api_response = api_instance.get_all_data_permissions(project_id, page=page, size=size, sort=sort)
        print("The response of DataPermissionsApi->get_all_data_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataPermissionsApi->get_all_data_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**DataPermissionPagedModelDTO**](DataPermissionPagedModelDTO.md)

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

# **get_data_permission_by_id**
> DataPermissionResponseDTO get_data_permission_by_id(project_id, id)

Gets data permission by id

Restricted to ADMIN project role that has the permission to update data permissions of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_permission_response_dto import DataPermissionResponseDTO
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
    api_instance = cm_python_openapi_sdk.DataPermissionsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the data permission

    try:
        # Gets data permission by id
        api_response = api_instance.get_data_permission_by_id(project_id, id)
        print("The response of DataPermissionsApi->get_data_permission_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataPermissionsApi->get_data_permission_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the data permission | 

### Return type

[**DataPermissionResponseDTO**](DataPermissionResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Data permission not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_permission_by_name**
> DataPermissionResponseDTO get_data_permission_by_name(project_id, name)

Gets data permission by name

Restricted to ADMIN project role that has the permission to update data permissions of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_permission_response_dto import DataPermissionResponseDTO
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
    api_instance = cm_python_openapi_sdk.DataPermissionsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'name_example' # str | Name of the data permission

    try:
        # Gets data permission by name
        api_response = api_instance.get_data_permission_by_name(project_id, name)
        print("The response of DataPermissionsApi->get_data_permission_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataPermissionsApi->get_data_permission_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the data permission | 

### Return type

[**DataPermissionResponseDTO**](DataPermissionResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Data permission not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_permission_by_id**
> DataPermissionResponseDTO update_data_permission_by_id(project_id, id, if_match, data_permission_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates data permission by id

Restricted to ADMIN project role that has the permission to update data permissions of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.data_permission_dto import DataPermissionDTO
from cm_python_openapi_sdk.models.data_permission_response_dto import DataPermissionResponseDTO
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
    api_instance = cm_python_openapi_sdk.DataPermissionsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the data permission
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    data_permission_dto = cm_python_openapi_sdk.DataPermissionDTO() # DataPermissionDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates data permission by id
        api_response = api_instance.update_data_permission_by_id(project_id, id, if_match, data_permission_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of DataPermissionsApi->update_data_permission_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataPermissionsApi->update_data_permission_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the data permission | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **data_permission_dto** | [**DataPermissionDTO**](DataPermissionDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**DataPermissionResponseDTO**](DataPermissionResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data permission was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Data permission not found |  -  |
**409** | Data permission with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

