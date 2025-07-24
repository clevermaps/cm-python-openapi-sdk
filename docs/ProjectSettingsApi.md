# cm_python_openapi_sdk.ProjectSettingsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_settings**](ProjectSettingsApi.md#create_project_settings) | **POST** /projects/{projectId}/md/projectSettings | Creates new project settings
[**delete_project_settings_by_id**](ProjectSettingsApi.md#delete_project_settings_by_id) | **DELETE** /projects/{projectId}/md/projectSettings/{id} | Deletes project settings by id
[**get_all_project_settings**](ProjectSettingsApi.md#get_all_project_settings) | **GET** /projects/{projectId}/md/projectSettings | Returns paged collection of all Project Settings objects in a project. This page will always contain only one object.
[**get_project_settings_by_id**](ProjectSettingsApi.md#get_project_settings_by_id) | **GET** /projects/{projectId}/md/projectSettings/{id} | Gets project settings by id
[**get_project_settings_by_name**](ProjectSettingsApi.md#get_project_settings_by_name) | **GET** /projects/{projectId}/md/projectSettings/{name} | Gets projectSettings by name
[**update_project_settings_by_id**](ProjectSettingsApi.md#update_project_settings_by_id) | **PUT** /projects/{projectId}/md/projectSettings/{id} | Updates project settings by id


# **create_project_settings**
> ProjectSettingsResponseDTO create_project_settings(project_id, project_settings_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new project settings

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_settings_dto import ProjectSettingsDTO
from cm_python_openapi_sdk.models.project_settings_response_dto import ProjectSettingsResponseDTO
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
    api_instance = cm_python_openapi_sdk.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    project_settings_dto = cm_python_openapi_sdk.ProjectSettingsDTO() # ProjectSettingsDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new project settings
        api_response = api_instance.create_project_settings(project_id, project_settings_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of ProjectSettingsApi->create_project_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->create_project_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **project_settings_dto** | [**ProjectSettingsDTO**](ProjectSettingsDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**ProjectSettingsResponseDTO**](ProjectSettingsResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project settings was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Project Settings object already exists in the project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_settings_by_id**
> delete_project_settings_by_id(project_id, id)

Deletes project settings by id

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
    api_instance = cm_python_openapi_sdk.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the project settings

    try:
        # Deletes project settings by id
        api_instance.delete_project_settings_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->delete_project_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the project settings | 

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
**204** | Project settings was successfully deleted |  -  |
**404** | Project settings not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_settings**
> ProjectSettingsPagedModelDTO get_all_project_settings(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Project Settings objects in a project. This page will always contain only one object.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_settings_paged_model_dto import ProjectSettingsPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Project Settings objects in a project. This page will always contain only one object.
        api_response = api_instance.get_all_project_settings(project_id, page=page, size=size, sort=sort)
        print("The response of ProjectSettingsApi->get_all_project_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->get_all_project_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**ProjectSettingsPagedModelDTO**](ProjectSettingsPagedModelDTO.md)

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

# **get_project_settings_by_id**
> ProjectSettingsResponseDTO get_project_settings_by_id(project_id, id)

Gets project settings by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_settings_response_dto import ProjectSettingsResponseDTO
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
    api_instance = cm_python_openapi_sdk.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the project settings

    try:
        # Gets project settings by id
        api_response = api_instance.get_project_settings_by_id(project_id, id)
        print("The response of ProjectSettingsApi->get_project_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->get_project_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the project settings | 

### Return type

[**ProjectSettingsResponseDTO**](ProjectSettingsResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Project settings not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_settings_by_name**
> ProjectSettingsResponseDTO get_project_settings_by_name(project_id, name)

Gets projectSettings by name

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_settings_response_dto import ProjectSettingsResponseDTO
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
    api_instance = cm_python_openapi_sdk.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'name_example' # str | Name of the projectSettings

    try:
        # Gets projectSettings by name
        api_response = api_instance.get_project_settings_by_name(project_id, name)
        print("The response of ProjectSettingsApi->get_project_settings_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->get_project_settings_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the projectSettings | 

### Return type

[**ProjectSettingsResponseDTO**](ProjectSettingsResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | ProjectSettings not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_settings_by_id**
> ProjectSettingsResponseDTO update_project_settings_by_id(project_id, id, if_match, project_settings_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates project settings by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_settings_dto import ProjectSettingsDTO
from cm_python_openapi_sdk.models.project_settings_response_dto import ProjectSettingsResponseDTO
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
    api_instance = cm_python_openapi_sdk.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the project settings
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    project_settings_dto = cm_python_openapi_sdk.ProjectSettingsDTO() # ProjectSettingsDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates project settings by id
        api_response = api_instance.update_project_settings_by_id(project_id, id, if_match, project_settings_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of ProjectSettingsApi->update_project_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->update_project_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the project settings | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **project_settings_dto** | [**ProjectSettingsDTO**](ProjectSettingsDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**ProjectSettingsResponseDTO**](ProjectSettingsResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project settings was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Project settings not found |  -  |
**409** | Project settings with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

