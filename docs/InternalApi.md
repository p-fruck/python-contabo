# pfruck_contabo.InternalApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket**](InternalApi.md#create_ticket) | **POST** /v1/create-ticket | Create a new support ticket
[**get_object_storage_credentials**](InternalApi.md#get_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/credentials | Get S3 compatible object storage credentials
[**regenerate_credentials**](InternalApi.md#regenerate_credentials) | **PATCH** /v1/users/{userId}/object-storages/credentials | Regenerates secret key of specified user for the S3 compatible object storages
[**retrieve_user_is_password_set**](InternalApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status


# **create_ticket**
> CreateTicketResponse create_ticket(x_request_id, create_ticket_request)

Create a new support ticket

Create a new support ticket.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import internal_api
from pfruck_contabo.model.create_ticket_request import CreateTicketRequest
from pfruck_contabo.model.create_ticket_response import CreateTicketResponse
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
    api_instance = internal_api.InternalApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_ticket_request = CreateTicketRequest(
        subject="Subject",
        note="Note",
    ) # CreateTicketRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new support ticket
        api_response = api_instance.create_ticket(x_request_id, create_ticket_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->create_ticket: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new support ticket
        api_response = api_instance.create_ticket(x_request_id, create_ticket_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->create_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **create_ticket_request** | [**CreateTicketRequest**](CreateTicketRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CreateTicketResponse**](CreateTicketResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard support ticket attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_credentials**
> CredentialResponse get_object_storage_credentials(x_request_id, user_id)

Get S3 compatible object storage credentials

Get S3 compatible object storage credentials for accessing it via S3 compatible tools like `aws` cli.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import internal_api
from pfruck_contabo.model.credential_response import CredentialResponse
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
    api_instance = internal_api.InternalApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get S3 compatible object storage credentials
        api_response = api_instance.get_object_storage_credentials(x_request_id, user_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->get_object_storage_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get S3 compatible object storage credentials
        api_response = api_instance.get_object_storage_credentials(x_request_id, user_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->get_object_storage_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **user_id** | **str**| The identifier of the user |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CredentialResponse**](CredentialResponse.md)

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

# **regenerate_credentials**
> CredentialResponse regenerate_credentials(x_request_id, user_id)

Regenerates secret key of specified user for the S3 compatible object storages

Regenerates secret key of specified user for the S3 compatible object storages. Please note that these credentials are valid for all object storages at different locations.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import internal_api
from pfruck_contabo.model.credential_response import CredentialResponse
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
    api_instance = internal_api.InternalApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The identifier of the user
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Regenerates secret key of specified user for the S3 compatible object storages
        api_response = api_instance.regenerate_credentials(x_request_id, user_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->regenerate_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Regenerates secret key of specified user for the S3 compatible object storages
        api_response = api_instance.regenerate_credentials(x_request_id, user_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->regenerate_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **user_id** | **str**| The identifier of the user |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CredentialResponse**](CredentialResponse.md)

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

# **retrieve_user_is_password_set**
> FindUserIsPasswordSetResponse retrieve_user_is_password_set(x_request_id)

Get user is password set status

Get info about idm user if the password is set.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import internal_api
from pfruck_contabo.model.find_user_is_password_set_response import FindUserIsPasswordSetResponse
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
    api_instance = internal_api.InternalApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    user_id = "6cdf5968-f9fe-4192-97c2-f349e813c5e8" # str | The user ID for checking if password is set for him (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user is password set status
        api_response = api_instance.retrieve_user_is_password_set(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->retrieve_user_is_password_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user is password set status
        api_response = api_instance.retrieve_user_is_password_set(x_request_id, x_trace_id=x_trace_id, user_id=user_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InternalApi->retrieve_user_is_password_set: %s\n" % e)
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

