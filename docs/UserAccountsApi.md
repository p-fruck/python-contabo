# pfruck_contabo.UserAccountsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_accounts**](UserAccountsApi.md#list_user_accounts) | **GET** /v1/me/accounts | List of your accounts
[**make_default_account**](UserAccountsApi.md#make_default_account) | **PATCH** /v1/me/account/{tenantId}/{customerId} | Make user account default
[**switch_account**](UserAccountsApi.md#switch_account) | **POST** /v1/me/action/switchAccount | Switch user account


# **list_user_accounts**
> ListUserSwitchAccountsResponse list_user_accounts(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, default=default)

List of your accounts

List of your accounts

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_user_switch_accounts_response import ListUserSwitchAccountsResponse
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
    api_instance = pfruck_contabo.UserAccountsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    email = 'john.doe@example.com' # str | Filter as substring match for user emails. (optional)
    default = true # bool | Filter if default account or not. (optional)

    try:
        # List of your accounts
        api_response = api_instance.list_user_accounts(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, default=default)
        print("The response of UserAccountsApi->list_user_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAccountsApi->list_user_accounts: %s\n" % e)
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
 **default** | **bool**| Filter if default account or not. | [optional] 

### Return type

[**ListUserSwitchAccountsResponse**](ListUserSwitchAccountsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains user account details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_default_account**
> UserSwitchAccountDefaultResponse make_default_account(x_request_id, tenant_id, customer_id, user_switch_account_default_request, x_trace_id=x_trace_id)

Make user account default

Make user account default

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.user_switch_account_default_request import UserSwitchAccountDefaultRequest
from pfruck_contabo.models.user_switch_account_default_response import UserSwitchAccountDefaultResponse
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
    api_instance = pfruck_contabo.UserAccountsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    tenant_id = 'DE' # str | Tenant ID.
    customer_id = '12345' # str | Customer ID.
    user_switch_account_default_request = pfruck_contabo.UserSwitchAccountDefaultRequest() # UserSwitchAccountDefaultRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Make user account default
        api_response = api_instance.make_default_account(x_request_id, tenant_id, customer_id, user_switch_account_default_request, x_trace_id=x_trace_id)
        print("The response of UserAccountsApi->make_default_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAccountsApi->make_default_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **tenant_id** | **str**| Tenant ID. | 
 **customer_id** | **str**| Customer ID. | 
 **user_switch_account_default_request** | [**UserSwitchAccountDefaultRequest**](UserSwitchAccountDefaultRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UserSwitchAccountDefaultResponse**](UserSwitchAccountDefaultResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains user account details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_account**
> UserSwitchAccountResponse switch_account(x_request_id, user_switch_account_request, x_trace_id=x_trace_id)

Switch user account

Switch user account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.user_switch_account_request import UserSwitchAccountRequest
from pfruck_contabo.models.user_switch_account_response import UserSwitchAccountResponse
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
    api_instance = pfruck_contabo.UserAccountsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_switch_account_request = pfruck_contabo.UserSwitchAccountRequest() # UserSwitchAccountRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Switch user account
        api_response = api_instance.switch_account(x_request_id, user_switch_account_request, x_trace_id=x_trace_id)
        print("The response of UserAccountsApi->switch_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAccountsApi->switch_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_switch_account_request** | [**UserSwitchAccountRequest**](UserSwitchAccountRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UserSwitchAccountResponse**](UserSwitchAccountResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains user account tokens. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

