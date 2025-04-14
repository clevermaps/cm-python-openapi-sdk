# cm_python_openapi_sdk.ProjectsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create new project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{projectId} | Delete project.
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /projects | Get list of projects for authenticated account.
[**get_project_by_id**](ProjectsApi.md#get_project_by_id) | **GET** /projects/{projectId} | Get project by given project id.
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{projectId} | Update the project.


# **create_project**
> ProjectResponseDTO create_project(create_project_dto)

Create new project

Create new project and set the authenticated user as the project member in ADMIN project role.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.create_project_dto import CreateProjectDTO
from cm_python_openapi_sdk.models.project_response_dto import ProjectResponseDTO
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
    api_instance = cm_python_openapi_sdk.ProjectsApi(api_client)
    create_project_dto = cm_python_openapi_sdk.CreateProjectDTO() # CreateProjectDTO | 

    try:
        # Create new project
        api_response = api_instance.create_project(create_project_dto)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_dto** | [**CreateProjectDTO**](CreateProjectDTO.md)|  | 

### Return type

[**ProjectResponseDTO**](ProjectResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project was successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Delete project.

**Security:**
Restricted to ADMIN project role.


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
    api_instance = cm_python_openapi_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project

    try:
        # Delete project.
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 

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
**204** | Project was successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> ProjectPagedModelDTO get_all_projects(organization_id=organization_id, page=page, size=size, sort=sort, share=share, expand=expand)

Get list of projects for authenticated account.

**Security:**
Resource returns only those projects where the authenticated user is a member.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_paged_model_dto import ProjectPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.ProjectsApi(api_client)
    organization_id = 'organization_id_example' # str | Id of the organization, used in query parameters (optional)
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)
    share = 'demo' # str | Filter project list by share attribute. (optional)
    expand = 'expand_example' # str | Expand selected attribute(s) to minimalize roundtrips. (optional)

    try:
        # Get list of projects for authenticated account.
        api_response = api_instance.get_all_projects(organization_id=organization_id, page=page, size=size, sort=sort, share=share, expand=expand)
        print("The response of ProjectsApi->get_all_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_all_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Id of the organization, used in query parameters | [optional] 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 
 **share** | **str**| Filter project list by share attribute. | [optional] 
 **expand** | **str**| Expand selected attribute(s) to minimalize roundtrips. | [optional] 

### Return type

[**ProjectPagedModelDTO**](ProjectPagedModelDTO.md)

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

# **get_project_by_id**
> ProjectResponseDTO get_project_by_id(project_id, expand=expand)

Get project by given project id.

**Security:**
Access is restricted only to users that are members of given project.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_response_dto import ProjectResponseDTO
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
    api_instance = cm_python_openapi_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    expand = 'expand_example' # str | Expand selected attribute(s) to minimalize roundtrips. (optional)

    try:
        # Get project by given project id.
        api_response = api_instance.get_project_by_id(project_id, expand=expand)
        print("The response of ProjectsApi->get_project_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **expand** | **str**| Expand selected attribute(s) to minimalize roundtrips. | [optional] 

### Return type

[**ProjectResponseDTO**](ProjectResponseDTO.md)

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

# **update_project**
> ProjectResponseDTO update_project(project_id, update_project_dto)

Update the project.

**Security:**
Restricted to ADMIN project role.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.project_response_dto import ProjectResponseDTO
from cm_python_openapi_sdk.models.update_project_dto import UpdateProjectDTO
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
    api_instance = cm_python_openapi_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    update_project_dto = cm_python_openapi_sdk.UpdateProjectDTO() # UpdateProjectDTO | 

    try:
        # Update the project.
        api_response = api_instance.update_project(project_id, update_project_dto)
        print("The response of ProjectsApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **update_project_dto** | [**UpdateProjectDTO**](UpdateProjectDTO.md)|  | 

### Return type

[**ProjectResponseDTO**](ProjectResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

