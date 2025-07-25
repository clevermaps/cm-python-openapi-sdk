# cm_python_openapi_sdk.MetricsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metric**](MetricsApi.md#create_metric) | **POST** /projects/{projectId}/md/metrics | Creates new metric.
[**delete_metric_by_id**](MetricsApi.md#delete_metric_by_id) | **DELETE** /projects/{projectId}/md/metrics/{id} | Deletes metric by id
[**get_all_metrics**](MetricsApi.md#get_all_metrics) | **GET** /projects/{projectId}/md/metrics | Returns paged collection of all Metrics in a project.
[**get_metric_by_id**](MetricsApi.md#get_metric_by_id) | **GET** /projects/{projectId}/md/metrics/{id} | Gets metric by id
[**get_metric_by_name**](MetricsApi.md#get_metric_by_name) | **GET** /projects/{projectId}/md/metrics/{name} | Gets metric by name
[**update_metric_by_id**](MetricsApi.md#update_metric_by_id) | **PUT** /projects/{projectId}/md/metrics/{id} | Updates metric by id


# **create_metric**
> MetricResponseDTO create_metric(project_id, metric_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new metric.

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.metric_dto import MetricDTO
from cm_python_openapi_sdk.models.metric_response_dto import MetricResponseDTO
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
    api_instance = cm_python_openapi_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    metric_dto = cm_python_openapi_sdk.MetricDTO() # MetricDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new metric.
        api_response = api_instance.create_metric(project_id, metric_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of MetricsApi->create_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->create_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **metric_dto** | [**MetricDTO**](MetricDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**MetricResponseDTO**](MetricResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Metric with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metric_by_id**
> delete_metric_by_id(project_id, id)

Deletes metric by id

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
    api_instance = cm_python_openapi_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the metric

    try:
        # Deletes metric by id
        api_instance.delete_metric_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling MetricsApi->delete_metric_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the metric | 

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
**204** | Metric was successfully deleted |  -  |
**404** | Metric not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_metrics**
> MetricPagedModelDTO get_all_metrics(project_id, page=page, size=size, sort=sort)

Returns paged collection of all Metrics in a project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.metric_paged_model_dto import MetricPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)

    try:
        # Returns paged collection of all Metrics in a project.
        api_response = api_instance.get_all_metrics(project_id, page=page, size=size, sort=sort)
        print("The response of MetricsApi->get_all_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_all_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 

### Return type

[**MetricPagedModelDTO**](MetricPagedModelDTO.md)

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

# **get_metric_by_id**
> MetricResponseDTO get_metric_by_id(project_id, id)

Gets metric by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.metric_response_dto import MetricResponseDTO
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
    api_instance = cm_python_openapi_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the metric

    try:
        # Gets metric by id
        api_response = api_instance.get_metric_by_id(project_id, id)
        print("The response of MetricsApi->get_metric_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metric_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the metric | 

### Return type

[**MetricResponseDTO**](MetricResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Metric not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric_by_name**
> MetricResponseDTO get_metric_by_name(project_id, name)

Gets metric by name

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.metric_response_dto import MetricResponseDTO
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
    api_instance = cm_python_openapi_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'name_example' # str | Name of the metric

    try:
        # Gets metric by name
        api_response = api_instance.get_metric_by_name(project_id, name)
        print("The response of MetricsApi->get_metric_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metric_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the metric | 

### Return type

[**MetricResponseDTO**](MetricResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Metric not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metric_by_id**
> MetricResponseDTO update_metric_by_id(project_id, id, if_match, metric_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates metric by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.metric_dto import MetricDTO
from cm_python_openapi_sdk.models.metric_response_dto import MetricResponseDTO
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
    api_instance = cm_python_openapi_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the metric
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    metric_dto = cm_python_openapi_sdk.MetricDTO() # MetricDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates metric by id
        api_response = api_instance.update_metric_by_id(project_id, id, if_match, metric_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of MetricsApi->update_metric_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->update_metric_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the metric | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **metric_dto** | [**MetricDTO**](MetricDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**MetricResponseDTO**](MetricResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Metric not found |  -  |
**409** | Metric with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

