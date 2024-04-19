# pfruck_contabo.UsersApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v1/users | Create a new user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete existing user by id
[**generate_client_secret**](UsersApi.md#generate_client_secret) | **PUT** /v1/users/client/secret | Generate new client secret
[**get_object_storage_credentials**](UsersApi.md#get_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/{objectStorageId}/credentials/{credentialId} | Get S3 compatible object storage credentials.
[**list_object_storage_credentials**](UsersApi.md#list_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/credentials | Get list of S3 compatible object storage credentials for user.
[**regenerate_object_storage_credentials**](UsersApi.md#regenerate_object_storage_credentials) | **PATCH** /v1/users/{userId}/object-storages/{objectStorageId}/credentials/{credentialId} | Regenerates secret key of specified user for the S3 compatible object storages.
[**resend_email_verification**](UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
[**reset_password**](UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
[**retrieve_user**](UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
[**retrieve_user_client**](UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
[**retrieve_user_list**](UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
[**update_user**](UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id


# **create_user**
> CreateUserResponse create_user(x_request_id, create_user_request)

Create a new user

Create a new user with required attributes name, email, enabled, totp (=Two-factor authentication 2FA), admin (=access to all endpoints and resources), accessAllResources and roles. You can't specify any password / secrets for the user. For security reasons the user will have to specify secrets on his own.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.create_user_request import CreateUserRequest
from pfruck_contabo.model.create_user_response import CreateUserResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_user_request = CreateUserRequest(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        enabled=False,
        totp=False,
        locale="de",
        roles=[1,2,3,4],
    ) # CreateUserRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new user
        api_response = api_instance.create_user(x_request_id, create_user_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new user
        api_response = api_instance.create_user(x_request_id, create_user_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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
> delete_user(x_request_id, user_id)

Delete existing user by id

By deleting a user he will not be able to access any endpoints or resources any longer. In order to temporarily disable a user please update its `enabled` attribute.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete existing user by id
        api_instance.delete_user(x_request_id, user_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete existing user by id
        api_instance.delete_user(x_request_id, user_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
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
> GenerateClientSecretResponse generate_client_secret(x_request_id)

Generate new client secret

Generate and get new client secret.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.generate_client_secret_response import GenerateClientSecretResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate new client secret
        api_response = api_instance.generate_client_secret(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->generate_client_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate new client secret
        api_response = api_instance.generate_client_secret(x_request_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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

# **get_object_storage_credentials**
> FindCredentialResponse get_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id)

Get S3 compatible object storage credentials.

Get S3 compatible object storage credentials for accessing it via S3 compatible tools like `aws` cli.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.find_credential_response import FindCredentialResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    object_storage_id = "d8417276-d2d9-43a9-a0a8-9a6fa6060246" # str | The identifier of the S3 object storage
    credential_id = 12345 # int | The ID of the object storage credential
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get S3 compatible object storage credentials.
        api_response = api_instance.get_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->get_object_storage_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get S3 compatible object storage credentials.
        api_response = api_instance.get_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->get_object_storage_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **user_id** | **str**| The identifier of the user. |
 **object_storage_id** | **str**| The identifier of the S3 object storage |
 **credential_id** | **int**| The ID of the object storage credential |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindCredentialResponse**](FindCredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains S3 credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object_storage_credentials**
> ListCredentialResponse list_object_storage_credentials(x_request_id, user_id)

Get list of S3 compatible object storage credentials for user.

Get list of S3 compatible object storage credentials for accessing it via S3 compatible tools like `aws` cli.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.list_credential_response import ListCredentialResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    object_storage_id = "d8417276-d2d9-43a9-a0a8-9a6fa6060246" # str | The identifier of the S3 object storage (optional)
    region_name = "Asia (Singapore)" # str | Filter for Object Storage by regions. Available regions: Asia (Singapore), European Union, United States (Central) (optional)
    display_name = "Object Storage EU 420" # str | Filter for Object Storage by his displayName. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get list of S3 compatible object storage credentials for user.
        api_response = api_instance.list_object_storage_credentials(x_request_id, user_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->list_object_storage_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of S3 compatible object storage credentials for user.
        api_response = api_instance.list_object_storage_credentials(x_request_id, user_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, region_name=region_name, display_name=display_name)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->list_object_storage_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **user_id** | **str**| The identifier of the user. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **object_storage_id** | **str**| The identifier of the S3 object storage | [optional]
 **region_name** | **str**| Filter for Object Storage by regions. Available regions: Asia (Singapore), European Union, United States (Central) | [optional]
 **display_name** | **str**| Filter for Object Storage by his displayName. | [optional]

### Return type

[**ListCredentialResponse**](ListCredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be an array of JSON objects that contains S3 credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_object_storage_credentials**
> FindCredentialResponse regenerate_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id)

Regenerates secret key of specified user for the S3 compatible object storages.

Regenerates secret key of specified user for the a specific S3 compatible object storages.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.find_credential_response import FindCredentialResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    object_storage_id = "d8417276-d2d9-43a9-a0a8-9a6fa6060246" # str | The identifier of the S3 object storage
    credential_id = 12345 # int | The ID of the object storage credential
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Regenerates secret key of specified user for the S3 compatible object storages.
        api_response = api_instance.regenerate_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->regenerate_object_storage_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Regenerates secret key of specified user for the S3 compatible object storages.
        api_response = api_instance.regenerate_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->regenerate_object_storage_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **user_id** | **str**| The identifier of the user. |
 **object_storage_id** | **str**| The identifier of the S3 object storage |
 **credential_id** | **int**| The ID of the object storage credential |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindCredentialResponse**](FindCredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains object storage S3 credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_verification**
> resend_email_verification(x_request_id, user_id)

Resend email verification

Resend email verification for a specific user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    redirect_url = "https://test.contabo.de" # str | The redirect url used for email verification (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resend email verification
        api_instance.resend_email_verification(x_request_id, user_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->resend_email_verification: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resend email verification
        api_instance.resend_email_verification(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)
    except pfruck_contabo.ApiException as e:
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
> reset_password(x_request_id, user_id)

Send reset password email

Send reset password email for a specific user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    redirect_url = "https://test.contabo.de" # str | The redirect url used for resetting password (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send reset password email
        api_instance.reset_password(x_request_id, user_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->reset_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send reset password email
        api_instance.reset_password(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)
    except pfruck_contabo.ApiException as e:
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
> FindUserResponse retrieve_user(x_request_id, user_id)

Get specific user by id

Get attributes for a specific user.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.find_user_response import FindUserResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific user by id
        api_response = api_instance.retrieve_user(x_request_id, user_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->retrieve_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific user by id
        api_response = api_instance.retrieve_user(x_request_id, user_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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
> FindClientResponse retrieve_user_client(x_request_id)

Get client

Get idm client.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.find_client_response import FindClientResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get client
        api_response = api_instance.retrieve_user_client(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->retrieve_user_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get client
        api_response = api_instance.retrieve_user_client(x_request_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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

# **retrieve_user_list**
> ListUserResponse retrieve_user_list(x_request_id)

List users

List and filter all your users.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.list_user_response import ListUserResponse
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    email = "john.doe@example.com" # str | Filter as substring match for user emails. (optional)
    enabled = True # bool | Filter if user is enabled or not. (optional)
    owner = True # bool | Filter if user is owner or not. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List users
        api_response = api_instance.retrieve_user_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->retrieve_user_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.retrieve_user_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, enabled=enabled, owner=owner)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->retrieve_user_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **email** | **str**| Filter as substring match for user emails. | [optional]
 **enabled** | **bool**| Filter if user is enabled or not. | [optional]
 **owner** | **bool**| Filter if user is owner or not. | [optional]

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
> UpdateUserResponse update_user(x_request_id, user_id, update_user_request)

Update specific user by id

Update attributes of a user. You may only specify the attributes you want to change. If an attribute is not set, it will retain its original value.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import users_api
from pfruck_contabo.model.update_user_response import UpdateUserResponse
from pfruck_contabo.model.update_user_request import UpdateUserRequest
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pfruck_contabo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user.
    update_user_request = UpdateUserRequest(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        enabled=False,
        totp=False,
        locale="de",
        roles=[1,2,3,4],
    ) # UpdateUserRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update specific user by id
        api_response = api_instance.update_user(x_request_id, user_id, update_user_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update specific user by id
        api_response = api_instance.update_user(x_request_id, user_id, update_user_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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

