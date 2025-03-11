# cm_python_openapi_sdk.AuthenticationApi

All URIs are relative to *https://staging.dev.clevermaps.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](AuthenticationApi.md#get_token) | **POST** /oauth/token | Get bearer token


# **get_token**
> TokenResponseDTO get_token(token_request_dto=token_request_dto)

Get bearer token

The token endpoint is used to obtain a Bearer token by presenting a valid Access token.

### Example


```python
import cm_python_openapi_sdk
from cm_python_openapi_sdk.models.token_request_dto import TokenRequestDTO
from cm_python_openapi_sdk.models.token_response_dto import TokenResponseDTO
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
    api_instance = cm_python_openapi_sdk.AuthenticationApi(api_client)
    token_request_dto = cm_python_openapi_sdk.TokenRequestDTO() # TokenRequestDTO |  (optional)

    try:
        # Get bearer token
        api_response = api_instance.get_token(token_request_dto=token_request_dto)
        print("The response of AuthenticationApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request_dto** | [**TokenRequestDTO**](TokenRequestDTO.md)|  | [optional] 

### Return type

[**TokenResponseDTO**](TokenResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

