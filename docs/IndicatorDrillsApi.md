# openapi_client.IndicatorDrillsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_indicator_drill**](IndicatorDrillsApi.md#create_indicator_drill) | **POST** /projects/{projectId}/md/indicatorDrills | Creates new Indicator Drill.
[**delete_indicator_drill_by_id**](IndicatorDrillsApi.md#delete_indicator_drill_by_id) | **DELETE** /projects/{projectId}/md/indicatorDrills/{id} | Deletes indicator drill by id
[**get_all_indicator_drills**](IndicatorDrillsApi.md#get_all_indicator_drills) | **GET** /projects/{projectId}/md/indicatorDrills | Returns paged collection of all Indicator Drills in a project.
[**get_indicator_drill_by_id**](IndicatorDrillsApi.md#get_indicator_drill_by_id) | **GET** /projects/{projectId}/md/indicatorDrills/{id} | Gets indicator drill by id
[**update_indicator_drill_by_id**](IndicatorDrillsApi.md#update_indicator_drill_by_id) | **PUT** /projects/{projectId}/md/indicatorDrills/{id} | Updates indicator drill by id


# **create_indicator_drill**
> IndicatorDrillDTO create_indicator_drill(project_id, indicator_drill_dto)

Creates new Indicator Drill.

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.indicator_drill_dto import IndicatorDrillDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IndicatorDrillsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    indicator_drill_dto = openapi_client.IndicatorDrillDTO() # IndicatorDrillDTO | 

    try:
        # Creates new Indicator Drill.
        api_response = api_instance.create_indicator_drill(project_id, indicator_drill_dto)
        print("The response of IndicatorDrillsApi->create_indicator_drill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorDrillsApi->create_indicator_drill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **indicator_drill_dto** | [**IndicatorDrillDTO**](IndicatorDrillDTO.md)|  | 

### Return type

[**IndicatorDrillDTO**](IndicatorDrillDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicator Drill was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Indicator Drill with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_indicator_drill_by_id**
> delete_indicator_drill_by_id(project_id, id)

Deletes indicator drill by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IndicatorDrillsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the indicator drill

    try:
        # Deletes indicator drill by id
        api_instance.delete_indicator_drill_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling IndicatorDrillsApi->delete_indicator_drill_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the indicator drill | 

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
**204** | Indicator Drill was successfully deleted |  -  |
**404** | Indicator Drill not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_indicator_drills**
> IndicatorDrillPagedModelDTO get_all_indicator_drills(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Indicator Drills in a project.

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.indicator_drill_paged_model_dto import IndicatorDrillPagedModelDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IndicatorDrillsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Indicator Drills in a project.
        api_response = api_instance.get_all_indicator_drills(project_id, page=page, size=size, sort=sort)
        print("The response of IndicatorDrillsApi->get_all_indicator_drills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorDrillsApi->get_all_indicator_drills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**IndicatorDrillPagedModelDTO**](IndicatorDrillPagedModelDTO.md)

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

# **get_indicator_drill_by_id**
> IndicatorDrillDTO get_indicator_drill_by_id(project_id, id)

Gets indicator drill by id

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.indicator_drill_dto import IndicatorDrillDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IndicatorDrillsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the indicator drill

    try:
        # Gets indicator drill by id
        api_response = api_instance.get_indicator_drill_by_id(project_id, id)
        print("The response of IndicatorDrillsApi->get_indicator_drill_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorDrillsApi->get_indicator_drill_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the indicator drill | 

### Return type

[**IndicatorDrillDTO**](IndicatorDrillDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Indicator Drill not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_indicator_drill_by_id**
> IndicatorDrillDTO update_indicator_drill_by_id(project_id, id, if_match, indicator_drill_dto)

Updates indicator drill by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.indicator_drill_dto import IndicatorDrillDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IndicatorDrillsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the indicator drill
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    indicator_drill_dto = openapi_client.IndicatorDrillDTO() # IndicatorDrillDTO | 

    try:
        # Updates indicator drill by id
        api_response = api_instance.update_indicator_drill_by_id(project_id, id, if_match, indicator_drill_dto)
        print("The response of IndicatorDrillsApi->update_indicator_drill_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndicatorDrillsApi->update_indicator_drill_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the indicator drill | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **indicator_drill_dto** | [**IndicatorDrillDTO**](IndicatorDrillDTO.md)|  | 

### Return type

[**IndicatorDrillDTO**](IndicatorDrillDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indicator Drill was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Indicator Drill not found |  -  |
**409** | Indicator Drill with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

