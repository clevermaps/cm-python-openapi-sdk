# cm_python_openapi_sdk.JobsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_status**](JobsApi.md#get_job_status) | **GET** /jobs/{jobId} | Get job status
[**get_jobs_history**](JobsApi.md#get_jobs_history) | **GET** /jobs/history | Get jobs history
[**submit_job_execution**](JobsApi.md#submit_job_execution) | **POST** /jobs | Submit job execution


# **get_job_status**
> JobDetailResponse get_job_status(job_id, type)

Get job status

Checks the current status of a given job.

### Job Statuses
- **RUNNING**: The job is currently running or waiting in the queue.
- **SUCCEEDED**: The job was successfully processed.
- **FAILED**: The job execution failed.
- **TIMED_OUT**: The job execution exceeded the allowed time limit.
- **ABORTED**: The job execution was manually or systemically aborted.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.job_detail_response import JobDetailResponse
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
    api_instance = cm_python_openapi_sdk.JobsApi(api_client)
    job_id = '15e41178-3933-422b-81fe-6ee9f48adab1' # str | job id is generated when submitting the job
    type = 'dataDump' # str | Jobs type

    try:
        # Get job status
        api_response = api_instance.get_job_status(job_id, type)
        print("The response of JobsApi->get_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| job id is generated when submitting the job | 
 **type** | **str**| Jobs type | 

### Return type

[**JobDetailResponse**](JobDetailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job successfully submitted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_history**
> JobHistoryPagedModelDTO get_jobs_history(project_id, account_id=account_id, sort_direction=sort_direction, last_evaluated_timestamp=last_evaluated_timestamp, type=type, dataset=dataset)

Get jobs history

Retrieves the job history for a project.

### Supported Job Types
- **dataPull**: Loads a CSV file into a dataset.
- **dataDump**: Dumps a dataset to a CSV file.
- **export**: Executes a DWH query and exports the result as a CSV file.
- **bulkPointQuery**: Executes DWH queries for a given list of points (latitude, longitude).
- **validate**: Validates the project.
- **truncate**: Truncates the project's data, dropping all DWH, metadata, and full-text search data.
- **importProject**: Imports a project into another one (server-side cloning).


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.job_history_paged_model_dto import JobHistoryPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.JobsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project, used as query parameter
    account_id = 'account_id_example' # str | Id of the account, used in query parameters (optional)
    sort_direction = 'ASC' # str | Sort direction (optional)
    last_evaluated_timestamp = '2020-11-18T08:39:56,199' # str | Last evaluated timestamp when requesting next page (UTC timestamp format) (optional)
    type = 'export' # str | Jobs type (optional)
    dataset = 'dataset_example' # str |  (optional)

    try:
        # Get jobs history
        api_response = api_instance.get_jobs_history(project_id, account_id=account_id, sort_direction=sort_direction, last_evaluated_timestamp=last_evaluated_timestamp, type=type, dataset=dataset)
        print("The response of JobsApi->get_jobs_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_jobs_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project, used as query parameter | 
 **account_id** | **str**| Id of the account, used in query parameters | [optional] 
 **sort_direction** | **str**| Sort direction | [optional] 
 **last_evaluated_timestamp** | **str**| Last evaluated timestamp when requesting next page (UTC timestamp format) | [optional] 
 **type** | **str**| Jobs type | [optional] 
 **dataset** | **str**|  | [optional] 

### Return type

[**JobHistoryPagedModelDTO**](JobHistoryPagedModelDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job_execution**
> JobDetailResponse submit_job_execution(general_job_request)

Submit job execution

Starts the execution of a new project task. Tasks are processed asynchronously, and all jobs are added to a queue.

### Supported Job Types
- **dataPull**: Loads a CSV file into a dataset.
- **dataDump**: Dumps a dataset to a CSV file.
- **export**: Executes a DWH query and exports the result as a CSV file.
- **bulkPointQuery**: Executes DWH queries for a given list of points (latitude, longitude); limited to 1,000 points per request.
- **validate**: Validates the project.
- **truncate**: Truncates the project's data, dropping all DWH, metadata, and full-text search data.
- **importProject**: Imports a project into another one (server-side cloning).

### Security
- **dataPull, importProject**: Requires `LOAD_DATA`, `DATA_EDITOR`, or `ADMIN` project roles.
- **dataDump, truncate**: Requires the `ADMIN` project role.
- **export, bulkPointQuery**: Requires `VIEWER`, `VIEW_CREATOR`, `METADATA_EDITOR`, `DATA_EDITOR`, `VIEW_CREATOR`, or `ADMIN` project roles.
- **validate**: Requires `METADATA_EDITOR`, `LOAD_DATA`, `DATA_EDITOR`, or `ADMIN` project roles.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.general_job_request import GeneralJobRequest
from cm_python_openapi_sdk.models.job_detail_response import JobDetailResponse
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
    api_instance = cm_python_openapi_sdk.JobsApi(api_client)
    general_job_request = cm_python_openapi_sdk.GeneralJobRequest() # GeneralJobRequest | Successful response

    try:
        # Submit job execution
        api_response = api_instance.submit_job_execution(general_job_request)
        print("The response of JobsApi->submit_job_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->submit_job_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **general_job_request** | [**GeneralJobRequest**](GeneralJobRequest.md)| Successful response | 

### Return type

[**JobDetailResponse**](JobDetailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job successfully submitted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

