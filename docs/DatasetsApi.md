# cm_python_openapi_sdk.DatasetsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetsApi.md#create_dataset) | **POST** /projects/{projectId}/md/datasets | Creates new dataset
[**delete_dataset_by_id**](DatasetsApi.md#delete_dataset_by_id) | **DELETE** /projects/{projectId}/md/datasets/{id} | Deletes dataset by id
[**generate_dataset_from_csv**](DatasetsApi.md#generate_dataset_from_csv) | **POST** /projects/{projectId}/md/datasets/generateDataset | Generate dataset from CSV
[**get_all_datasets**](DatasetsApi.md#get_all_datasets) | **GET** /projects/{projectId}/md/datasets | Returns paged collection of all datasets in a project
[**get_dataset_by_id**](DatasetsApi.md#get_dataset_by_id) | **GET** /projects/{projectId}/md/datasets/{id} | Gets dataset by id
[**update_dataset_by_id**](DatasetsApi.md#update_dataset_by_id) | **PUT** /projects/{projectId}/md/datasets/{id} | Updates dataset by id


# **create_dataset**
> DatasetDTO create_dataset(project_id, dataset_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Creates new dataset

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dataset_dto import DatasetDTO
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
    api_instance = cm_python_openapi_sdk.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    dataset_dto = cm_python_openapi_sdk.DatasetDTO() # DatasetDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Creates new dataset
        api_response = api_instance.create_dataset(project_id, dataset_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of DatasetsApi->create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **dataset_dto** | [**DatasetDTO**](DatasetDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset was successfully created |  -  |
**400** | Syntax errors or validation violations |  -  |
**409** | Datasets with the same name or id already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_by_id**
> delete_dataset_by_id(project_id, id)

Deletes dataset by id

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
    api_instance = cm_python_openapi_sdk.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the dataset

    try:
        # Deletes dataset by id
        api_instance.delete_dataset_by_id(project_id, id)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_dataset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the dataset | 

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
**204** | Dataset was successfully deleted |  -  |
**404** | Dataset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_dataset_from_csv**
> DatasetDTO generate_dataset_from_csv(project_id, name, body, subtype=subtype, primary_key=primary_key, geometry=geometry, csv_separator=csv_separator, csv_quote=csv_quote, csv_escape=csv_escape)

Generate dataset from CSV

Generate dataset metadata object from a CSV file with a header. The CSV body must not be longer than 10 lines.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dataset_dto import DatasetDTO
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
    api_instance = cm_python_openapi_sdk.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    name = 'baskets' # str | Name of the dataset
    body = 'body_example' # str | 
    subtype = 'basic' # str | Subtype of the dataset (optional) (default to 'basic')
    primary_key = 'basic_id' # str | Name of the property that will be marked as primary key (optional)
    geometry = 'geometry_example' # str | Name of the geometry key for geometryPolygon dataset subtype (optional)
    csv_separator = ',' # str | Custom CSV column separator character (optional) (default to ',')
    csv_quote = '"' # str | Custom CSV quote character (optional) (default to '"')
    csv_escape = '\\' # str | Custom CSV escape character (optional) (default to '\\')

    try:
        # Generate dataset from CSV
        api_response = api_instance.generate_dataset_from_csv(project_id, name, body, subtype=subtype, primary_key=primary_key, geometry=geometry, csv_separator=csv_separator, csv_quote=csv_quote, csv_escape=csv_escape)
        print("The response of DatasetsApi->generate_dataset_from_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->generate_dataset_from_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **name** | **str**| Name of the dataset | 
 **body** | **str**|  | 
 **subtype** | **str**| Subtype of the dataset | [optional] [default to &#39;basic&#39;]
 **primary_key** | **str**| Name of the property that will be marked as primary key | [optional] 
 **geometry** | **str**| Name of the geometry key for geometryPolygon dataset subtype | [optional] 
 **csv_separator** | **str**| Custom CSV column separator character | [optional] [default to &#39;,&#39;]
 **csv_quote** | **str**| Custom CSV quote character | [optional] [default to &#39;&quot;&#39;]
 **csv_escape** | **str**| Custom CSV escape character | [optional] [default to &#39;\\&#39;]

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | When a parameter is invalid, or CSV body parsing fails, or the CSV does not contain specific columns |  -  |
**409** | When the specified name of the dataset already exists |  -  |
**413** | When the CSV body is larger than 10 lines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_datasets**
> DatasetPagedModelDTO get_all_datasets(project_id, page=page, size=size, sort=sort, type=type)

Returns paged collection of all datasets in a project

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dataset_paged_model_dto import DatasetPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    page = 0 # int | Number of the page (optional) (default to 0)
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)
    type = 'type_example' # str | Returns only collection of datasets of given type. (optional)

    try:
        # Returns paged collection of all datasets in a project
        api_response = api_instance.get_all_datasets(project_id, page=page, size=size, sort=sort, type=type)
        print("The response of DatasetsApi->get_all_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_all_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **page** | **int**| Number of the page | [optional] [default to 0]
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 
 **type** | **str**| Returns only collection of datasets of given type. | [optional] 

### Return type

[**DatasetPagedModelDTO**](DatasetPagedModelDTO.md)

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

# **get_dataset_by_id**
> DatasetDTO get_dataset_by_id(project_id, id)

Gets dataset by id

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dataset_dto import DatasetDTO
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
    api_instance = cm_python_openapi_sdk.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the dataset

    try:
        # Gets dataset by id
        api_response = api_instance.get_dataset_by_id(project_id, id)
        print("The response of DatasetsApi->get_dataset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the dataset | 

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Dataset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_by_id**
> DatasetDTO update_dataset_by_id(project_id, id, if_match, dataset_dto, x_can_strict_json_validation=x_can_strict_json_validation)

Updates dataset by id

Restricted to EDITOR project role that has the permission to update metadata of the project.

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.dataset_dto import DatasetDTO
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
    api_instance = cm_python_openapi_sdk.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    id = 'id_example' # str | Id of the dataset
    if_match = 'if_match_example' # str | ETag value used for conditional updates
    dataset_dto = cm_python_openapi_sdk.DatasetDTO() # DatasetDTO | 
    x_can_strict_json_validation = False # bool |  (optional) (default to False)

    try:
        # Updates dataset by id
        api_response = api_instance.update_dataset_by_id(project_id, id, if_match, dataset_dto, x_can_strict_json_validation=x_can_strict_json_validation)
        print("The response of DatasetsApi->update_dataset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->update_dataset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **id** | **str**| Id of the dataset | 
 **if_match** | **str**| ETag value used for conditional updates | 
 **dataset_dto** | [**DatasetDTO**](DatasetDTO.md)|  | 
 **x_can_strict_json_validation** | **bool**|  | [optional] [default to False]

### Return type

[**DatasetDTO**](DatasetDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset was successfully updated |  -  |
**400** | Syntax error or validation violations |  -  |
**404** | Dataset not found |  -  |
**409** | Dataset with the same name or id already exists |  -  |
**412** | Version provided in If-Match header is outdated |  -  |
**428** | Version was not provided in If-Match header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

