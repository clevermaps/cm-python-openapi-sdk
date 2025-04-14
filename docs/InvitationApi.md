# cm_python_openapi_sdk.InvitationApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_project_invitation**](InvitationApi.md#accept_project_invitation) | **POST** /invitations/{invitationHash} | Accept invitation.
[**get_invitation**](InvitationApi.md#get_invitation) | **GET** /invitations/{invitationHash} | Get detail of an invitation.


# **accept_project_invitation**
> InvitationDTO accept_project_invitation(invitation_hash)

Accept invitation.

This resource allows accepting an invitation by an invited user.
The URL contains a secret `invitationHash` that is sent to the invited user by email.
By clicking on the href link from the invitation email, the user is redirected into the CleverMaps application, and after authentication, the invitation is accepted.

When a user accepts an invitation, they are added as a new Member of the Project in the role granted by the invitation.

**Security:**
Restricted to invited user. The authenticated user email must equal the email in the invitation.


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
    api_instance = cm_python_openapi_sdk.InvitationApi(api_client)
    invitation_hash = 'invitation_hash_example' # str | Hash of the invitation

    try:
        # Accept invitation.
        api_response = api_instance.accept_project_invitation(invitation_hash)
        print("The response of InvitationApi->accept_project_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->accept_project_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_hash** | **str**| Hash of the invitation | 

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
**400** | invitation cannot be accepted (unexpected invitation state - already accepted, canceled) |  -  |
**403** | authenticated user email does not match email in invitation |  -  |
**404** | invitation was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation**
> InvitationDTO get_invitation(invitation_hash)

Get detail of an invitation.

An invitation status value is one of:
- PENDING
- ACCEPTED
- CANCELED
- EXPIRED


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
    api_instance = cm_python_openapi_sdk.InvitationApi(api_client)
    invitation_hash = 'invitation_hash_example' # str | Hash of the invitation

    try:
        # Get detail of an invitation.
        api_response = api_instance.get_invitation(invitation_hash)
        print("The response of InvitationApi->get_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->get_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_hash** | **str**| Hash of the invitation | 

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

