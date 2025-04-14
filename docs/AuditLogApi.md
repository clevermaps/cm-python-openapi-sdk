# cm_python_openapi_sdk.AuditLogApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_event**](AuditLogApi.md#get_audit_log_event) | **GET** /auditlog/{eventId} | Get audit log event by eventId
[**get_audit_logs**](AuditLogApi.md#get_audit_logs) | **GET** /auditlog | Get audit logs for project


# **get_audit_log_event**
> AuditLogSingleResource get_audit_log_event(event_id, project_id)

Get audit log event by eventId

Get audit log event by event ID for project.

**Security:**
Resource return only audit log events for those projects where the authenticated user is Admin.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.audit_log_single_resource import AuditLogSingleResource
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
    api_instance = cm_python_openapi_sdk.AuditLogApi(api_client)
    event_id = '49608916084546516127288104563488184528966319983011299378' # str | Event ID
    project_id = 'project_id_example' # str | Id of the project, used as query parameter

    try:
        # Get audit log event by eventId
        api_response = api_instance.get_audit_log_event(event_id, project_id)
        print("The response of AuditLogApi->get_audit_log_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_log_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Event ID | 
 **project_id** | **str**| Id of the project, used as query parameter | 

### Return type

[**AuditLogSingleResource**](AuditLogSingleResource.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single audit log event |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs**
> AuditLogPagedResource get_audit_logs(project_id, account_id=account_id, event_types=event_types, var_from=var_from, to=to, last_evaluated_event_id=last_evaluated_event_id, last_evaluated_timestamp=last_evaluated_timestamp, page_size=page_size, sort_direction=sort_direction)

Get audit logs for project

Get audit logs for project

**Security:**
Resource return only audit log for those projects where the authenticated user is Admin.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.audit_log_paged_resource import AuditLogPagedResource
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
    api_instance = cm_python_openapi_sdk.AuditLogApi(api_client)
    project_id = 'project_id_example' # str | Id of the project, used as query parameter
    account_id = 'account_id_example' # str | Id of the account, used in query parameters (optional)
    event_types = 'search' # str | Event type (optional)
    var_from = '2019-01-17T19:09:28,918' # str | Timestamp lower bound (UTC timestamp format) (optional)
    to = '2022-01-17T19:09:28,918' # str | Timestamp upper bound (UTC timestamp format) (optional)
    last_evaluated_event_id = 'last_evaluated_event_id_example' # str | Last evaluated event ID when requesting next page (optional)
    last_evaluated_timestamp = '2020-11-18T08:39:56,199' # str | Last evaluated timestamp when requesting next page (UTC timestamp format) (optional)
    page_size = 56 # int | page size (optional)
    sort_direction = 'ASC' # str | Sort direction (optional)

    try:
        # Get audit logs for project
        api_response = api_instance.get_audit_logs(project_id, account_id=account_id, event_types=event_types, var_from=var_from, to=to, last_evaluated_event_id=last_evaluated_event_id, last_evaluated_timestamp=last_evaluated_timestamp, page_size=page_size, sort_direction=sort_direction)
        print("The response of AuditLogApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project, used as query parameter | 
 **account_id** | **str**| Id of the account, used in query parameters | [optional] 
 **event_types** | **str**| Event type | [optional] 
 **var_from** | **str**| Timestamp lower bound (UTC timestamp format) | [optional] 
 **to** | **str**| Timestamp upper bound (UTC timestamp format) | [optional] 
 **last_evaluated_event_id** | **str**| Last evaluated event ID when requesting next page | [optional] 
 **last_evaluated_timestamp** | **str**| Last evaluated timestamp when requesting next page (UTC timestamp format) | [optional] 
 **page_size** | **int**| page size | [optional] 
 **sort_direction** | **str**| Sort direction | [optional] 

### Return type

[**AuditLogPagedResource**](AuditLogPagedResource.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged collection of audit logs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

