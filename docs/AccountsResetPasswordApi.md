# cm_python_openapi_sdk.AccountsResetPasswordApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_password_with_token**](AccountsResetPasswordApi.md#reset_password_with_token) | **POST** /accounts/passwordReset/{passwordResetToken} | Finish reset password with token
[**send_reset_password_token**](AccountsResetPasswordApi.md#send_reset_password_token) | **POST** /accounts/passwordReset | Ask for reset password token
[**verify_reset_password_token**](AccountsResetPasswordApi.md#verify_reset_password_token) | **GET** /accounts/passwordReset/{passwordResetToken} | Verify reset password token is valid


# **reset_password_with_token**
> reset_password_with_token(password_reset_token, reset_password_dto=reset_password_dto)

Finish reset password with token

Finish the process of resetting the password by sending a valid token and a new password.
**Security:**
Unauthorized resource, anonymous users are allowed to finish password reset.


### Example


```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.reset_password_dto import ResetPasswordDTO
from cm_python_openapi_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = cm_python_openapi_sdk.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)


# Enter a context with an instance of the API client
with cm_python_openapi_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cm_python_openapi_sdk.AccountsResetPasswordApi(api_client)
    password_reset_token = 'password_reset_token_example' # str | Password reset token
    reset_password_dto = cm_python_openapi_sdk.ResetPasswordDTO() # ResetPasswordDTO |  (optional)

    try:
        # Finish reset password with token
        api_instance.reset_password_with_token(password_reset_token, reset_password_dto=reset_password_dto)
    except Exception as e:
        print("Exception when calling AccountsResetPasswordApi->reset_password_with_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_token** | **str**| Password reset token | 
 **reset_password_dto** | [**ResetPasswordDTO**](ResetPasswordDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Password was reset to new password |  -  |
**404** | Request token was not found |  -  |
**400** | New password does not match requirements for passwords (see changePassword for requirements) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_reset_password_token**
> send_reset_password_token(send_reset_password_dto=send_reset_password_dto)

Ask for reset password token

Create new request for resetting password.

**Security:**
Unauthorized resource, anonymous users are allowed to initiate password reset.


### Example


```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.send_reset_password_dto import SendResetPasswordDTO
from cm_python_openapi_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = cm_python_openapi_sdk.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)


# Enter a context with an instance of the API client
with cm_python_openapi_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cm_python_openapi_sdk.AccountsResetPasswordApi(api_client)
    send_reset_password_dto = cm_python_openapi_sdk.SendResetPasswordDTO() # SendResetPasswordDTO |  (optional)

    try:
        # Ask for reset password token
        api_instance.send_reset_password_token(send_reset_password_dto=send_reset_password_dto)
    except Exception as e:
        print("Exception when calling AccountsResetPasswordApi->send_reset_password_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_reset_password_dto** | [**SendResetPasswordDTO**](SendResetPasswordDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created request for resetting password |  -  |
**404** | No account was found for given email |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_reset_password_token**
> AccountDTO verify_reset_password_token(password_reset_token)

Verify reset password token is valid

Test if given token exists and is valid. Returns account which password is resetting.

**Security:**
Unauthorized resource, anonymous users are allowed to verify password reset token.


### Example


```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.account_dto import AccountDTO
from cm_python_openapi_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://staging.dev.clevermaps.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = cm_python_openapi_sdk.Configuration(
    host = "https://staging.dev.clevermaps.io/rest"
)


# Enter a context with an instance of the API client
with cm_python_openapi_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cm_python_openapi_sdk.AccountsResetPasswordApi(api_client)
    password_reset_token = 'password_reset_token_example' # str | Password reset token

    try:
        # Verify reset password token is valid
        api_response = api_instance.verify_reset_password_token(password_reset_token)
        print("The response of AccountsResetPasswordApi->verify_reset_password_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsResetPasswordApi->verify_reset_password_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_token** | **str**| Password reset token | 

### Return type

[**AccountDTO**](AccountDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about account |  -  |
**404** | Request token was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

