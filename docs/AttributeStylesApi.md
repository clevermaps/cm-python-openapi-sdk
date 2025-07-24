# cm_python_openapi_sdk.AttributeStylesApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute_style**](AttributeStylesApi.md#create_attribute_style) | **POST** /projects/{projectId}/md/attributeStyles | Creates new attribute style
[**delete_attribute_style_by_id**](AttributeStylesApi.md#delete_attribute_style_by_id) | **DELETE** /projects/{projectId}/md/attributeStyles/{id} | Deletes attribute style by id
[**get_all_attribute_styles**](AttributeStylesApi.md#get_all_attribute_styles) | **GET** /projects/{projectId}/md/attributeStyles | Returns paged collection of all Attribute Styles in a project
[**get_attribute_style_by_id**](AttributeStylesApi.md#get_attribute_style_by_id) | **GET** /projects/{projectId}/md/attributeStyles/{id} | Gets attribute style by id
[**get_attribute_style_by_name**](AttributeStylesApi.md#get_attribute_style_by_name) | **GET** /projects/{projectId}/md/attributeStyles/{name} | Gets attribute style by name
[**update_attribute_style_by_id**](AttributeStylesApi.md#update_attribute_style_by_id) | **PUT** /projects/{projectId}/md/attributeStyles/{id} | Updates attribute style by id


# **create_attribute_style**
> AttributeStyleResponseDTO create_attribute_style(project_id, attribute_style_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new attribute style

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.attribute_style_dto import AttributeStyleDTO
from cm_python_openapi_sdk.models.attribute_style_response_dto import AttributeStyleResponseDTO
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
    api_instance = cm_python_openapi_sdk.AttributeStylesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    attribute_style_dto = cm_python_openapi_sdk.AttributeStyleDTO() # AttributeStyleDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new attribute style
        api_response = api_instance.create_attribute_style(project_id, attribute_style_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of AttributeStylesApi->create_attribute_style:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributeStylesApi->create_attribute_style: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **attribute_style_dto** | [**AttributeStyleDTO**](AttributeStyleDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**AttributeStyleResponseDTO**](AttributeStyleResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute style was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Attribute style with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_style_by_id**
> delete_attribute_style_by_id(project_id, id)

Deletes attribute style by id

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
    api_instance = cm_python_openapi_sdk.AttributeStylesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the attribute style

    try:
        # Deletes attribute style by id
        api_instance.delete_attribute_style_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling AttributeStylesApi->delete_attribute_style_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the attribute style | 

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
**204** | Attribute style was successfully deleted |  -  |
**404** | Attribute style not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_attribute_styles**
> AttributeStylePagedModelDTO get_all_attribute_styles(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Attribute Styles in a project

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.attribute_style_paged_model_dto import AttributeStylePagedModelDTO
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
    api_instance = cm_python_openapi_sdk.AttributeStylesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Attribute Styles in a project
        api_response = api_instance.get_all_attribute_styles(project_id, page=page, size=size, sort=sort)
        print("The response of AttributeStylesApi->get_all_attribute_styles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributeStylesApi->get_all_attribute_styles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**AttributeStylePagedModelDTO**](AttributeStylePagedModelDTO.md)

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

# **get_attribute_style_by_id**
> AttributeStyleResponseDTO get_attribute_style_by_id(project_id, id)

Gets attribute style by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.attribute_style_response_dto import AttributeStyleResponseDTO
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
    api_instance = cm_python_openapi_sdk.AttributeStylesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the attribute style

    try:
        # Gets attribute style by id
        api_response = api_instance.get_attribute_style_by_id(project_id, id)
        print("The response of AttributeStylesApi->get_attribute_style_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributeStylesApi->get_attribute_style_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the attribute style | 

### Return type

[**AttributeStyleResponseDTO**](AttributeStyleResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Attribute style not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_style_by_name**
> AttributeStyleResponseDTO get_attribute_style_by_name(project_id, name)

Gets attribute style by name

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.attribute_style_response_dto import AttributeStyleResponseDTO
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
    api_instance = cm_python_openapi_sdk.AttributeStylesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'name_example' # str | Name of the attribute style

    try:
        # Gets attribute style by name
        api_response = api_instance.get_attribute_style_by_name(project_id, name)
        print("The response of AttributeStylesApi->get_attribute_style_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributeStylesApi->get_attribute_style_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the attribute style | 

### Return type

[**AttributeStyleResponseDTO**](AttributeStyleResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Attribute style not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_style_by_id**
> AttributeStyleResponseDTO update_attribute_style_by_id(project_id, id, if_match, attribute_style_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates attribute style by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.attribute_style_dto import AttributeStyleDTO
from cm_python_openapi_sdk.models.attribute_style_response_dto import AttributeStyleResponseDTO
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
    api_instance = cm_python_openapi_sdk.AttributeStylesApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the attribute style
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    attribute_style_dto = cm_python_openapi_sdk.AttributeStyleDTO() # AttributeStyleDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates attribute style by id
        api_response = api_instance.update_attribute_style_by_id(project_id, id, if_match, attribute_style_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of AttributeStylesApi->update_attribute_style_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributeStylesApi->update_attribute_style_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the attribute style | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **attribute_style_dto** | [**AttributeStyleDTO**](AttributeStyleDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**AttributeStyleResponseDTO**](AttributeStyleResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute style was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Attribute style not found |  -  |
**409** | Attribute style with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

