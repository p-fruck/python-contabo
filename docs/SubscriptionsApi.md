# pfruck_contabo.SubscriptionsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_windows**](SubscriptionsApi.md#activate_windows) | **POST** /v1/subscriptions/activate-windows | Activate the windows licence.
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /v1/subscriptions/cancel/{tenantId}/{subscriptionId} | Cancel the subscription.
[**get_earliest_cancellation_date**](SubscriptionsApi.md#get_earliest_cancellation_date) | **GET** /v1/subscriptions/{tenantId}/{subscriptionId} | Get earliest cancellation date
[**retrieve_subscription**](SubscriptionsApi.md#retrieve_subscription) | **GET** /v1/subscriptions/type/{subscriptionType}/{tenantId}/{objectId} | Retrieve specific subscription
[**retrieve_subscriptions**](SubscriptionsApi.md#retrieve_subscriptions) | **GET** /v1/subscriptions/type/{subscriptionType}/{tenantId} | List all subscriptions by type
[**revoke_subscription_cancellation**](SubscriptionsApi.md#revoke_subscription_cancellation) | **DELETE** /v1/subscriptions/type/{subscriptionType}/{tenantId}/{objectId}/cancel | Revoke cancellation


# **activate_windows**
> ActivateWindowsResponse activate_windows(x_request_id, activate_windows_request)

Activate the windows licence.

Activate the windows licence of the given mak

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import subscriptions_api
from pfruck_contabo.model.activate_windows_response import ActivateWindowsResponse
from pfruck_contabo.model.activate_windows_request import ActivateWindowsRequest
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    activate_windows_request = ActivateWindowsRequest(
        mak="mak_example",
    ) # ActivateWindowsRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Activate the windows licence.
        api_response = api_instance.activate_windows(x_request_id, activate_windows_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->activate_windows: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activate the windows licence.
        api_response = api_instance.activate_windows(x_request_id, activate_windows_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->activate_windows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **activate_windows_request** | [**ActivateWindowsRequest**](ActivateWindowsRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**ActivateWindowsResponse**](ActivateWindowsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will include the updated licence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription**
> CancelSubscriptionResponse cancel_subscription(x_request_id, subscription_id, tenant_id, cancel_subscription_request)

Cancel the subscription.

Cancel the subscription given by the subscription Id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import subscriptions_api
from pfruck_contabo.model.cancel_subscription_response import CancelSubscriptionResponse
from pfruck_contabo.model.cancel_subscription_request import CancelSubscriptionRequest
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    subscription_id = "vserver-67890" # str | The identifier of the subscription
    tenant_id = "INT or DE" # str | The tenant identifier
    cancel_subscription_request = CancelSubscriptionRequest(
        reason="reason_example",
        reason_id=3.14,
    ) # CancelSubscriptionRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel the subscription.
        api_response = api_instance.cancel_subscription(x_request_id, subscription_id, tenant_id, cancel_subscription_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel the subscription.
        api_response = api_instance.cancel_subscription(x_request_id, subscription_id, tenant_id, cancel_subscription_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **subscription_id** | **str**| The identifier of the subscription |
 **tenant_id** | **str**| The tenant identifier |
 **cancel_subscription_request** | [**CancelSubscriptionRequest**](CancelSubscriptionRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CancelSubscriptionResponse**](CancelSubscriptionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a link to the subscription and the cancel date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earliest_cancellation_date**
> EarliestCancellationDateSubscriptionResponse get_earliest_cancellation_date(x_request_id, subscription_id, tenant_id)

Get earliest cancellation date

get the earliest cancellation date after the given date

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import subscriptions_api
from pfruck_contabo.model.earliest_cancellation_date_subscription_response import EarliestCancellationDateSubscriptionResponse
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    subscription_id = "vserver-67890" # str | The identifier of the subscription
    tenant_id = "INT or DE" # str | The tenant identifier
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get earliest cancellation date
        api_response = api_instance.get_earliest_cancellation_date(x_request_id, subscription_id, tenant_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->get_earliest_cancellation_date: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get earliest cancellation date
        api_response = api_instance.get_earliest_cancellation_date(x_request_id, subscription_id, tenant_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->get_earliest_cancellation_date: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **subscription_id** | **str**| The identifier of the subscription |
 **tenant_id** | **str**| The tenant identifier |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**EarliestCancellationDateSubscriptionResponse**](EarliestCancellationDateSubscriptionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the earliest cancellation date after the given date. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_subscription**
> FindSubscriptionResponse retrieve_subscription(x_request_id, subscription_type, tenant_id, object_id)

Retrieve specific subscription

Retrieve specific subscription by subscription id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import subscriptions_api
from pfruck_contabo.model.find_subscription_response import FindSubscriptionResponse
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    subscription_type = None # bool, date, datetime, dict, float, int, list, str, none_type | The type of the subscription
    tenant_id = "INT or DE" # str | The tenant identifier
    object_id = "12345" # str | The identifier of the object
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve specific subscription
        api_response = api_instance.retrieve_subscription(x_request_id, subscription_type, tenant_id, object_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->retrieve_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve specific subscription
        api_response = api_instance.retrieve_subscription(x_request_id, subscription_type, tenant_id, object_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->retrieve_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **subscription_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| The type of the subscription |
 **tenant_id** | **str**| The tenant identifier |
 **object_id** | **str**| The identifier of the object |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindSubscriptionResponse**](FindSubscriptionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains aspecific subscription for a customer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_subscriptions**
> ListSubscriptionsResponse retrieve_subscriptions(x_request_id, subscription_type, tenant_id)

List all subscriptions by type

List all subscriptions by type for a customer

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import subscriptions_api
from pfruck_contabo.model.list_subscriptions_response import ListSubscriptionsResponse
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    subscription_type = None # bool, date, datetime, dict, float, int, list, str, none_type | The type of the subscription
    tenant_id = "INT or DE" # str | The tenant identifier
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all subscriptions by type
        api_response = api_instance.retrieve_subscriptions(x_request_id, subscription_type, tenant_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->retrieve_subscriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all subscriptions by type
        api_response = api_instance.retrieve_subscriptions(x_request_id, subscription_type, tenant_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->retrieve_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **subscription_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| The type of the subscription |
 **tenant_id** | **str**| The tenant identifier |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]

### Return type

[**ListSubscriptionsResponse**](ListSubscriptionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the list of all subscriptions for a customer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_subscription_cancellation**
> revoke_subscription_cancellation(x_request_id, subscription_type, tenant_id, object_id)

Revoke cancellation

Revokes the cancellation of the subscription given by the subscription Id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import subscriptions_api
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    subscription_type = None # bool, date, datetime, dict, float, int, list, str, none_type | The type of the subscription
    tenant_id = "INT or DE" # str | The tenant identifier
    object_id = "12345" # str | The identifier of the object
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Revoke cancellation
        api_instance.revoke_subscription_cancellation(x_request_id, subscription_type, tenant_id, object_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->revoke_subscription_cancellation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Revoke cancellation
        api_instance.revoke_subscription_cancellation(x_request_id, subscription_type, tenant_id, object_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling SubscriptionsApi->revoke_subscription_cancellation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **subscription_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| The type of the subscription |
 **tenant_id** | **str**| The tenant identifier |
 **object_id** | **str**| The identifier of the object |
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
**204** | The response will be 204 OK if the cancellation was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

