# cm_python_openapi_sdk.ProjectInvitationsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invitation**](ProjectInvitationsApi.md#create_invitation) | **POST** /projects/{projectId}/invitations | Create new invitation to the project for a user.
[**delete_invitation**](ProjectInvitationsApi.md#delete_invitation) | **DELETE** /projects/{projectId}/invitations/{invitationId} | Delete invitation.
[**get_invitation_by_id**](ProjectInvitationsApi.md#get_invitation_by_id) | **GET** /projects/{projectId}/invitations/{invitationId} | Get detail of an invitation.
[**get_invitations**](ProjectInvitationsApi.md#get_invitations) | **GET** /projects/{projectId}/invitations | Get list of project invitations.
[**update_invitation**](ProjectInvitationsApi.md#update_invitation) | **PUT** /projects/{projectId}/invitations/{invitationId} | Update invitation.


# **create_invitation**
> InvitationDTO create_invitation(project_id, create_invitation)

Create new invitation to the project for a user.

User is specified by email address and invitation contains a project role.  **Security:** Restricted to ADMIN project role. 

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.create_invitation import CreateInvitation
from cm_python_openapi_sdk.models.invitation_dto import InvitationDTO
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
    api_instance = cm_python_openapi_sdk.ProjectInvitationsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    create_invitation = cm_python_openapi_sdk.CreateInvitation() # CreateInvitation | 

    try:
        # Create new invitation to the project for a user.
        api_response = api_instance.create_invitation(project_id, create_invitation)
        print("The response of ProjectInvitationsApi->create_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInvitationsApi->create_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **create_invitation** | [**CreateInvitation**](CreateInvitation.md)|  | 

### Return type

[**InvitationDTO**](InvitationDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New invitation was created and sent to email. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invitation**
> InvitationDTO delete_invitation(project_id, invitation_id)

Delete invitation.

If an invitation has status `PENDING`, project Admin can cancel it by calling the `DELETE` method. Calling the `DELETE` method is equivalent to sending a `PUT` request with the status `CANCELED` as described above.  **Security:** Restricted to ADMIN project role. 

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.invitation_dto import InvitationDTO
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
    api_instance = cm_python_openapi_sdk.ProjectInvitationsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    invitation_id = 'invitation_id_example' # str | Id of the invitation

    try:
        # Delete invitation.
        api_response = api_instance.delete_invitation(project_id, invitation_id)
        print("The response of ProjectInvitationsApi->delete_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInvitationsApi->delete_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **invitation_id** | **str**| Id of the invitation | 

### Return type

[**InvitationDTO**](InvitationDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation_by_id**
> InvitationDTO get_invitation_by_id(project_id, invitation_id)

Get detail of an invitation.

An invitation status value is one of: - PENDING - ACCEPTED - CANCELED - EXPIRED  **Security:** Restricted to ADMIN project role. 

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.invitation_dto import InvitationDTO
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
    api_instance = cm_python_openapi_sdk.ProjectInvitationsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    invitation_id = 'invitation_id_example' # str | Id of the invitation

    try:
        # Get detail of an invitation.
        api_response = api_instance.get_invitation_by_id(project_id, invitation_id)
        print("The response of ProjectInvitationsApi->get_invitation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInvitationsApi->get_invitation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **invitation_id** | **str**| Id of the invitation | 

### Return type

[**InvitationDTO**](InvitationDTO.md)

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

# **get_invitations**
> InvitationPagedModelDTO get_invitations(project_id, size=size, page=page, sort=sort, status=status)

Get list of project invitations.

**Security:** Restricted to ADMIN project role. 

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.invitation_paged_model_dto import InvitationPagedModelDTO
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
    api_instance = cm_python_openapi_sdk.ProjectInvitationsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    size = 100 # int | The count of records to return for one page (optional) (default to 100)
    page = 0 # int | Number of the page (optional) (default to 0)
    sort = 'name,desc' # str | Name of the attribute to use for sorting the results, together with direction (asc or desc) (optional)
    status = 'ACCEPTED' # str | Filter invitations by status attribute. (optional)

    try:
        # Get list of project invitations.
        api_response = api_instance.get_invitations(project_id, size=size, page=page, sort=sort, status=status)
        print("The response of ProjectInvitationsApi->get_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInvitationsApi->get_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **size** | **int**| The count of records to return for one page | [optional] [default to 100]
 **page** | **int**| Number of the page | [optional] [default to 0]
 **sort** | **str**| Name of the attribute to use for sorting the results, together with direction (asc or desc) | [optional] 
 **status** | **str**| Filter invitations by status attribute. | [optional] 

### Return type

[**InvitationPagedModelDTO**](InvitationPagedModelDTO.md)

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

# **update_invitation**
> InvitationDTO update_invitation(project_id, invitation_id, update_invitation)

Update invitation.

Cancel or resend project invitation. If an invitation has status `PENDING`, project Admin can cancel it. If the invitation has status `CANCELED`, `EXPIRED` or `PENDING`, user can activate it or resend the invitation email by PUTing the status `PENDING`.  Invitations with status `ACCEPTED` cannot be updated anymore.       **Allowed status transitions:**  | Original Status | PUT Request | New Status | |---------------|------------|------------| | CANCELED      | PENDING    | PENDING    | | EXPIRED      | PENDING    | PENDING    | | PENDING      | CANCELED   | CANCELED   |  **Security:** Restricted to ADMIN project role. 

### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.invitation_dto import InvitationDTO
from cm_python_openapi_sdk.models.update_invitation import UpdateInvitation
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
    api_instance = cm_python_openapi_sdk.ProjectInvitationsApi(api_client)
    project_id = 'project_id_example' # str | Id of the project
    invitation_id = 'invitation_id_example' # str | Id of the invitation
    update_invitation = cm_python_openapi_sdk.UpdateInvitation() # UpdateInvitation | 

    try:
        # Update invitation.
        api_response = api_instance.update_invitation(project_id, invitation_id, update_invitation)
        print("The response of ProjectInvitationsApi->update_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectInvitationsApi->update_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of the project | 
 **invitation_id** | **str**| Id of the invitation | 
 **update_invitation** | [**UpdateInvitation**](UpdateInvitation.md)|  | 

### Return type

[**InvitationDTO**](InvitationDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful update |  -  |
**400** | Invitation cannot be updated (unexpected invitation state - already accepted, canceled) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

