# cm_python_openapi_sdk.IndicatorsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_indicator**](IndicatorsApi.md#create_indicator) | **POST** /projects/{projectId}/md/indicators | Creates new Indicator.
[**delete_indicator_by_id**](IndicatorsApi.md#delete_indicator_by_id) | **DELETE** /projects/{projectId}/md/indicators/{id} | Deletes indicator by id
[**get_all_indicators**](IndicatorsApi.md#get_all_indicators) | **GET** /projects/{projectId}/md/indicators | Returns paged collection of all Indicators in a project.
[**get_indicator_by_id**](IndicatorsApi.md#get_indicator_by_id) | **GET** /projects/{projectId}/md/indicators/{id} | Gets indicator by id
[**get_indicator_by_name**](IndicatorsApi.md#get_indicator_by_name) | **GET** /projects/{projectId}/md/indicators/{name} | Gets indicator by name
[**update_indicator_by_id**](IndicatorsApi.md#update_indicator_by_id) | **PUT** /projects/{projectId}/md/indicators/{id} | Updates indicator by id


# **create_indicator**
> IndicatorResponseDTO create_indicator(project_id, indicator_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new Indicator.

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.indicator_dto import IndicatorDTO
from cm_python_openapi_sdk.models.indicator_response_dto import IndicatorResponseDTO
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
    api_instance = cm_python_openapi_sdk.IndicatorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    indicator_dto = cm_python_openapi_sdk.IndicatorDTO() # IndicatorDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new Indicator.
        api_response = api_instance.create_indicator(project_id, indicator_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of IndicatorsApi->create_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->create_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **indicator_dto** | [**IndicatorDTO**](IndicatorDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**IndicatorResponseDTO**](IndicatorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicator was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Indicator with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_indicator_by_id**
> delete_indicator_by_id(project_id, id)

Deletes indicator by id

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
    api_instance = cm_python_openapi_sdk.IndicatorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the indicator

    try:
        # Deletes indicator by id
        api_instance.delete_indicator_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling IndicatorsApi->delete_indicator_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the indicator | 

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
**204** | Indicator was successfully deleted |  -  |
**404** | Indicator not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_indicators**
> IndicatorPagedModelDTO get_all_indicators(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Indicators in a project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.indicator_paged_model_dto import IndicatorPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.IndicatorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Indicators in a project.
        api_response = api_instance.get_all_indicators(project_id, page=page, size=size, sort=sort)
        print("The response of IndicatorsApi->get_all_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_all_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**IndicatorPagedModelDTO**](IndicatorPagedModelDTO.md)

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

# **get_indicator_by_id**
> IndicatorResponseDTO get_indicator_by_id(project_id, id)

Gets indicator by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.indicator_response_dto import IndicatorResponseDTO
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
    api_instance = cm_python_openapi_sdk.IndicatorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the indicator

    try:
        # Gets indicator by id
        api_response = api_instance.get_indicator_by_id(project_id, id)
        print("The response of IndicatorsApi->get_indicator_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_indicator_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the indicator | 

### Return type

[**IndicatorResponseDTO**](IndicatorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Indicator not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_by_name**
> IndicatorResponseDTO get_indicator_by_name(project_id, name)

Gets indicator by name

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.indicator_response_dto import IndicatorResponseDTO
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
    api_instance = cm_python_openapi_sdk.IndicatorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'name_example' # str | Name of the indicator

    try:
        # Gets indicator by name
        api_response = api_instance.get_indicator_by_name(project_id, name)
        print("The response of IndicatorsApi->get_indicator_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->get_indicator_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the indicator | 

### Return type

[**IndicatorResponseDTO**](IndicatorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Indicator not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_indicator_by_id**
> IndicatorResponseDTO update_indicator_by_id(project_id, id, if_match, indicator_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates indicator by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.indicator_dto import IndicatorDTO
from cm_python_openapi_sdk.models.indicator_response_dto import IndicatorResponseDTO
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
    api_instance = cm_python_openapi_sdk.IndicatorsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the indicator
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    indicator_dto = cm_python_openapi_sdk.IndicatorDTO() # IndicatorDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates indicator by id
        api_response = api_instance.update_indicator_by_id(project_id, id, if_match, indicator_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of IndicatorsApi->update_indicator_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorsApi->update_indicator_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the indicator | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **indicator_dto** | [**IndicatorDTO**](IndicatorDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**IndicatorResponseDTO**](IndicatorResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicator was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Indicator not found |  -  |
**409** | Indicator with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

