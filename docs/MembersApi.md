# cm_python_openapi_sdk.MembersApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_member**](MembersApi.md#add_project_member) | **POST** /projects/{projectId}/members | Add new project member and assign a role.
[**delete_membership**](MembersApi.md#delete_membership) | **DELETE** /projects/{projectId}/members/{membershipId} | Deletes membership of user in project.
[**get_membership_by_id**](MembersApi.md#get_membership_by_id) | **GET** /projects/{projectId}/members/{membershipId} | Get detail of user membership in project by membership id.
[**get_project_members**](MembersApi.md#get_project_members) | **GET** /projects/{projectId}/members | Get list of project members.
[**update_membership**](MembersApi.md#update_membership) | **PUT** /projects/{projectId}/members/{membershipId} | Update membership by changing role or status in project.


# **add_project_member**
> MembershipResponseDTO add_project_member(project_id, create_membership_dto)

Add new project member and assign a role.

The user is added into the project without any cooperation (acknowledgement) with invited user. You can add user
by accountId or email.

See the Project Invitation resource too. It allows to invite a new member by email address and sends an invitation email.

**Security:**
Restricted to ADMIN project role.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.create_membership_dto import CreateMembershipDTO
from cm_python_openapi_sdk.models.membership_response_dto import MembershipResponseDTO
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
    api_instance = cm_python_openapi_sdk.MembersApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    create_membership_dto = cm_python_openapi_sdk.CreateMembershipDTO() # CreateMembershipDTO | 

    try:
        # Add new project member and assign a role.
        api_response = api_instance.add_project_member(project_id, create_membership_dto)
        print("The response of MembersApi->add_project_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->add_project_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **create_membership_dto** | [**CreateMembershipDTO**](CreateMembershipDTO.md)|  | 

### Return type

[**MembershipResponseDTO**](MembershipResponseDTO.md)

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

# **delete_membership**
> delete_membership(project_id, membership_id)

Deletes membership of user in project.

The user will be not able to access the project anymore.

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
    api_instance = cm_python_openapi_sdk.MembersApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    membership_id = 'membership_id_example' # str | Id of the membership

    try:
        # Deletes membership of user in project.
        api_instance.delete_membership(project_id, membership_id)
    except Exception as e:
        print("Exception when calling MembersApi->delete_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **membership_id** | **str**| Id of the membership | 

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
**204** | Membership was successfully deleted |  -  |
**400** | Deletion of the last project ADMIN denied. There always needs to be at least one user in ADMIN role in each project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_by_id**
> MembershipResponseDTO get_membership_by_id(project_id, membership_id)

Get detail of user membership in project by membership id.

**Security:**
Restricted to ADMIN project role.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.membership_response_dto import MembershipResponseDTO
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
    api_instance = cm_python_openapi_sdk.MembersApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    membership_id = 'membership_id_example' # str | Id of the membership

    try:
        # Get detail of user membership in project by membership id.
        api_response = api_instance.get_membership_by_id(project_id, membership_id)
        print("The response of MembersApi->get_membership_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->get_membership_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **membership_id** | **str**| Id of the membership | 

### Return type

[**MembershipResponseDTO**](MembershipResponseDTO.md)

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

# **get_project_members**
> GetProjectMembers200Response get_project_members(project_id, size=size, page=page, sort=sort, expand=expand, account_id=account_id)

Get list of project members.

See list of user role: https://docs.clevermaps.io/docs/projects-and-users#UserrolesandPermissions-Userroles

**Security:**
Restricted to ADMIN project role, unless `accountId` is provided. See Constraints for more info

Constraints:
- If `accountId` is provided, other query parameters (`size`, `sort`, etc.) must NOT be used. Also endpoint will return single member.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.get_project_members200_response import GetProjectMembers200Response
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
    api_instance = cm_python_openapi_sdk.MembersApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    page = 0 # int | Number of the page (optional) (default to 0)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)
    expand = 'expand_example' # str | Expand selected attribute(s) to minimalize roundtrips. (optional)
    account_id = 'account_id_example' # str | Id of the account, used in query parameters (optional)

    try:
        # Get list of project members.
        api_response = api_instance.get_project_members(project_id, size=size, page=page, sort=sort, expand=expand, account_id=account_id)
        print("The response of MembersApi->get_project_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->get_project_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **page** | **int**| Number of the page | [optional] [default to 0]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 
 **expand** | **str**| Expand selected attribute(s) to minimalize roundtrips. | [optional] 
 **account_id** | **str**| Id of the account, used in query parameters | [optional] 

### Return type

[**GetProjectMembers200Response**](GetProjectMembers200Response.md)

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

# **update_membership**
> MembershipResponseDTO update_membership(project_id, membership_id, update_membership_dto)

Update membership by changing role or status in project.

**Security:**
Restricted to ADMIN project role.


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.membership_response_dto import MembershipResponseDTO
from cm_python_openapi_sdk.models.update_membership_dto import UpdateMembershipDTO
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
    api_instance = cm_python_openapi_sdk.MembersApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    membership_id = 'membership_id_example' # str | Id of the membership
    update_membership_dto = cm_python_openapi_sdk.UpdateMembershipDTO() # UpdateMembershipDTO | 

    try:
        # Update membership by changing role or status in project.
        api_response = api_instance.update_membership(project_id, membership_id, update_membership_dto)
        print("The response of MembersApi->update_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->update_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **membership_id** | **str**| Id of the membership | 
 **update_membership_dto** | [**UpdateMembershipDTO**](UpdateMembershipDTO.md)|  | 

### Return type

[**MembershipResponseDTO**](MembershipResponseDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update |  -  |
**400** | Update of the last project ADMIN denied. There always needs to be at least one user in ADMIN role in each project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

