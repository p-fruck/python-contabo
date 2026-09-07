# pfruck_contabo.UsersApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v1/users | Create a new user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete existing user by id
[**generate_client_secret**](UsersApi.md#generate_client_secret) | **PUT** /v1/users/client/secret | Generate new client secret
[**generate_sso_token**](UsersApi.md#generate_sso_token) | **POST** /v1/users/sso-token | Generate one time SSO token
[**request_email_change**](UsersApi.md#request_email_change) | **POST** /v1/users/{userId}/mail-change-requests | Request email change
[**resend_email_verification**](UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
[**reset_password**](UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
[**retrieve_user**](UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
[**retrieve_user_client**](UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
[**retrieve_user_is_password_set**](UsersApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status
[**retrieve_user_list**](UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
[**update_user**](UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id


# **create_user**
> CreateUserResponse create_user(x_request_id, create_user_request, x_trace_id=x_trace_id)

Create a new user

Create a new user with required attributes firstName, lastName, email, enabled, totp (=Two-factor authentication 2FA), admin (=access to all endpoints and resources), accessAllResources and roles. You can't specify any password / secrets for the user. For security reasons the user will have to specify secrets on his own.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.create_user_request import CreateUserRequest
from pfruck_contabo.models.create_user_response import CreateUserResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_user_request = pfruck_contabo.CreateUserRequest() # CreateUserRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create a new user
        api_response = api_instance.create_user(x_request_id, create_user_request, x_trace_id=x_trace_id)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard user attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(x_request_id, user_id, x_trace_id=x_trace_id)

Delete existing user by id

By deleting a user he will not be able to access any endpoints or resources any longer. In order to temporarily disable a user please update its `enabled` attribute.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Delete existing user by id
        api_instance.delete_user(x_request_id, user_id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body has no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_client_secret**
> GenerateClientSecretResponse generate_client_secret(x_request_id, x_trace_id=x_trace_id)

Generate new client secret

Generate and get new client secret.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.generate_client_secret_response import GenerateClientSecretResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Generate new client secret
        api_response = api_instance.generate_client_secret(x_request_id, x_trace_id=x_trace_id)
        print("The response of UsersApi->generate_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->generate_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**GenerateClientSecretResponse**](GenerateClientSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains new client secret. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sso_token**
> FindSsoTokenResponse generate_sso_token(x_request_id, x_trace_id=x_trace_id)

Generate one time SSO token

Generate an one time SSO token for the authenticated user account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_sso_token_response import FindSsoTokenResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Generate one time SSO token
        api_response = api_instance.generate_sso_token(x_request_id, x_trace_id=x_trace_id)
        print("The response of UsersApi->generate_sso_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->generate_sso_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindSsoTokenResponse**](FindSsoTokenResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The generated one time SSO token payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_email_change**
> request_email_change(x_request_id, user_id, x_trace_id=x_trace_id)

Request email change

Request an email change for the specified user. This operation is only available for owner accounts. If triggered by a subuser, the request will be rejected.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Request email change
        api_instance.request_email_change(x_request_id, user_id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling UsersApi->request_email_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body has no content |  -  |
**403** | Forbidden |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_verification**
> resend_email_verification(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)

Resend email verification

Resend email verification for a specific user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    redirect_url = 'https://test.contabo.de' # str | The redirect url used for email verification (optional)

    try:
        # Resend email verification
        api_instance.resend_email_verification(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)
    except Exception as e:
        print("Exception when calling UsersApi->resend_email_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **redirect_url** | **str**| The redirect url used for email verification | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body has no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)

Send reset password email

Send reset password email for a specific user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    redirect_url = 'https://test.contabo.de' # str | The redirect url used for resetting password (optional)

    try:
        # Send reset password email
        api_instance.reset_password(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)
    except Exception as e:
        print("Exception when calling UsersApi->reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **redirect_url** | **str**| The redirect url used for resetting password | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body has no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user**
> FindUserResponse retrieve_user(x_request_id, user_id, x_trace_id=x_trace_id)

Get specific user by id

Get attributes for a specific user.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_user_response import FindUserResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get specific user by id
        api_response = api_instance.retrieve_user(x_request_id, user_id, x_trace_id=x_trace_id)
        print("The response of UsersApi->retrieve_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->retrieve_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindUserResponse**](FindUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard user attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_client**
> FindClientResponse retrieve_user_client(x_request_id, x_trace_id=x_trace_id)

Get client

Get idm client.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_client_response import FindClientResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get client
        api_response = api_instance.retrieve_user_client(x_request_id, x_trace_id=x_trace_id)
        print("The response of UsersApi->retrieve_user_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->retrieve_user_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindClientResponse**](FindClientResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard client attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_is_password_set**
> FindUserIsPasswordSetResponse retrieve_user_is_password_set(x_request_id, x_trace_id=x_trace_id, user_id=user_id)

Get user is password set status

Get info about idm user if the password is set.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_user_is_password_set_response import FindUserIsPasswordSetResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The user ID for checking if password is set for him (optional)

    try:
        # Get user is password set status
        api_response = api_instance.retrieve_user_is_password_set(x_request_id, x_trace_id=x_trace_id, user_id=user_id)
        print("The response of UsersApi->retrieve_user_is_password_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->retrieve_user_is_password_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **user_id** | **str**| The user ID for checking if password is set for him | [optional] 

### Return type

[**FindUserIsPasswordSetResponse**](FindUserIsPasswordSetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard user attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_list**
> ListUserResponse retrieve_user_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, enabled=enabled, default=default, owner=owner, search=search)

List users

List and filter all your users.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_user_response import ListUserResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    email = 'john.doe@example.com' # str | Filter as substring match for user emails. (optional)
    enabled = true # bool | Filter if user is enabled or not. (optional)
    default = true # bool | Filter if user is default account or not. (optional)
    owner = true # bool | Filter if user is owner or not. (optional)
    search = 'John Doe' # str | Full text search when listing the users. Can be searched by `first name`, `last name`, `email` or `first name` and `last name` combined (optional)

    try:
        # List users
        api_response = api_instance.retrieve_user_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, enabled=enabled, default=default, owner=owner, search=search)
        print("The response of UsersApi->retrieve_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->retrieve_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **email** | **str**| Filter as substring match for user emails. | [optional] 
 **enabled** | **bool**| Filter if user is enabled or not. | [optional] 
 **default** | **bool**| Filter if user is default account or not. | [optional] 
 **owner** | **bool**| Filter if user is owner or not. | [optional] 
 **search** | **str**| Full text search when listing the users. Can be searched by &#x60;first name&#x60;, &#x60;last name&#x60;, &#x60;email&#x60; or &#x60;first name&#x60; and &#x60;last name&#x60; combined | [optional] 

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of users. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UpdateUserResponse update_user(x_request_id, user_id, update_user_request, x_trace_id=x_trace_id)

Update specific user by id

Update attributes of a user. You may only specify the attributes you want to change. If an attribute is not set, it will retain its original value.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.update_user_request import UpdateUserRequest
from pfruck_contabo.models.update_user_response import UpdateUserResponse
from pfruck_contabo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.contabo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pfruck_contabo.Configuration(
    host = "https://api.contabo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = pfruck_contabo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pfruck_contabo.UsersApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    update_user_request = pfruck_contabo.UpdateUserRequest() # UpdateUserRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update specific user by id
        api_response = api_instance.update_user(x_request_id, user_id, update_user_request, x_trace_id=x_trace_id)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard user attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

