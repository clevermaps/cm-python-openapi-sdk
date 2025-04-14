# cm_python_openapi_sdk.AccountsApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_onboarding**](AccountsApi.md#change_onboarding) | **PUT** /accounts/{accountId}/onboarding | Change account onboarding
[**change_password**](AccountsApi.md#change_password) | **PUT** /accounts/{accountId}/password | Change password
[**change_preferences**](AccountsApi.md#change_preferences) | **PUT** /accounts/{accountId}/preferences | Change account preferences
[**delete_account_by_id**](AccountsApi.md#delete_account_by_id) | **DELETE** /accounts/{accountId} | Delete account.
[**get_account_by_account_id**](AccountsApi.md#get_account_by_account_id) | **GET** /accounts/{accountId} | Get account by accountId
[**get_account_by_email**](AccountsApi.md#get_account_by_email) | **GET** /accounts | Find if account with email exists.
[**get_current_account**](AccountsApi.md#get_current_account) | **GET** /accounts/current | Get current account.
[**register_account**](AccountsApi.md#register_account) | **POST** /accounts | Register new account


# **change_onboarding**
> change_onboarding(account_id, account_onboarding_parameters=account_onboarding_parameters)

Change account onboarding

Section of account profile for tracking onboarding steps for each user. It has two sections:
- `introShown` - tracks the project views that were already visited by current user
- `tipsShown` - list of unique tips that were already presented to current user
**Security:**
User is allowed to change only it's own onboarding. Bearer token must match `accountId`


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.account_onboarding_parameters import AccountOnboardingParameters
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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Id of the account
    account_onboarding_parameters = cm_python_openapi_sdk.AccountOnboardingParameters() # AccountOnboardingParameters |  (optional)

    try:
        # Change account onboarding
        api_instance.change_onboarding(account_id, account_onboarding_parameters=account_onboarding_parameters)
    except Exception as e:
        print("Exception when calling AccountsApi->change_onboarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Id of the account | 
 **account_onboarding_parameters** | [**AccountOnboardingParameters**](AccountOnboardingParameters.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Onboarding changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> change_password(account_id, password_change_dto=password_change_dto)

Change password

Set password for user Account. New password must match all of following restrictions:
- minimal length 8 characters
- must contains at least one uppercase character
- must contains at least one lowercase character
- must contains at least one numeric character

**Security:**
User is allowed to change only it's own password. Bearer token must match `accountId`


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.password_change_dto import PasswordChangeDTO
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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Id of the account
    password_change_dto = cm_python_openapi_sdk.PasswordChangeDTO() # PasswordChangeDTO |  (optional)

    try:
        # Change password
        api_instance.change_password(account_id, password_change_dto=password_change_dto)
    except Exception as e:
        print("Exception when calling AccountsApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Id of the account | 
 **password_change_dto** | [**PasswordChangeDTO**](PasswordChangeDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Password changed |  -  |
**400** | Bad request, new password does not match requirements for password or old password is invalid |  -  |
**403** | accountId does not match user account provided in bearer token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_preferences**
> change_preferences(account_id, account_preferences=account_preferences)

Change account preferences

Preferences for user Account. Structure contains currently two keys:
- language - preferred language for user (supported values: "en", "cs")
- lastActiveProject - project that was last active for a user Both these preferences are used by CleverMaps Client JavaScript application and have no direct impact on backend behaviour.

Updates the preferences by merge. If some of preference keys is not present, value of this key is not reset.

**Security:**
User is allowed to change only it's own preferences. Bearer token must match `accountId`


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.account_preferences import AccountPreferences
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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Id of the account
    account_preferences = cm_python_openapi_sdk.AccountPreferences() # AccountPreferences |  (optional)

    try:
        # Change account preferences
        api_instance.change_preferences(account_id, account_preferences=account_preferences)
    except Exception as e:
        print("Exception when calling AccountsApi->change_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Id of the account | 
 **account_preferences** | [**AccountPreferences**](AccountPreferences.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Preferences changed |  -  |
**403** | accountId does not match user account provided in bearer token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_by_id**
> delete_account_by_id(account_id)

Delete account.

Deletes user account from Okta. Destroys Okta session. Delete from Intercom.

**Security:**
User can delete only himself.


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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Id of the account

    try:
        # Delete account.
        api_instance.delete_account_by_id(account_id)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Id of the account | 

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
**204** | Account was successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_account_id**
> GetAccountByAccountId200Response get_account_by_account_id(account_id)

Get account by accountId

Account for user identified accountId. The resource has two type of responses:
- full account detail (for request on currently authenticated account)
- restricted account detail - when getting details about another user
  - `accountId`, `fullName`, `language` and `status` properties are returned


### Example

* Bearer Authentication (bearerAuth):

```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.get_account_by_account_id200_response import GetAccountByAccountId200Response
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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    account_id = 'account_id_example' # str | Id of the account

    try:
        # Get account by accountId
        api_response = api_instance.get_account_by_account_id(account_id)
        print("The response of AccountsApi->get_account_by_account_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_by_account_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Id of the account | 

### Return type

[**GetAccountByAccountId200Response**](GetAccountByAccountId200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_email**
> get_account_by_email(email)

Find if account with email exists.

Find if account with email exists. Search is limited on `ENABLED` accounts.


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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    email = 'john.smith@clevermaps.io' # str | Email address

    try:
        # Find if account with email exists.
        api_instance.get_account_by_email(email)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address | 

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
**204** | Account with email exists |  -  |
**404** | Account with email not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_account**
> AccountDTO get_current_account()

Get current account.

Account for user identified by Bearer token. Resource is the same as the `/rest/accounts/{accountId}`.


### Example

* Bearer Authentication (bearerAuth):

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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)

    try:
        # Get current account.
        api_response = api_instance.get_current_account()
        print("The response of AccountsApi->get_current_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_current_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountDTO**](AccountDTO.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_account**
> AccountDTO register_account(new_account_dto)

Register new account

### Example


```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.account_dto import AccountDTO
from cm_python_openapi_sdk.models.new_account_dto import NewAccountDTO
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
    api_instance = cm_python_openapi_sdk.AccountsApi(api_client)
    new_account_dto = cm_python_openapi_sdk.NewAccountDTO() # NewAccountDTO | 

    try:
        # Register new account
        api_response = api_instance.register_account(new_account_dto)
        print("The response of AccountsApi->register_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->register_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_account_dto** | [**NewAccountDTO**](NewAccountDTO.md)|  | 

### Return type

[**AccountDTO**](AccountDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account was successfully registered |  -  |
**409** | Account with this email already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

