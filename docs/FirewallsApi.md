# pfruck_contabo.FirewallsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall**](FirewallsApi.md#create_firewall) | **POST** /v1/firewalls | Create a new firewall
[**delete_firewall**](FirewallsApi.md#delete_firewall) | **DELETE** /v1/firewalls/{firewallId} | Delete existing Firewall by id
[**patch_firewall**](FirewallsApi.md#patch_firewall) | **PATCH** /v1/firewalls/{firewallId} | Update a Firewall by id
[**put_firewall**](FirewallsApi.md#put_firewall) | **PUT** /v1/firewalls/{firewallId} | Update specific firewall rules
[**retrieve_firewall**](FirewallsApi.md#retrieve_firewall) | **GET** /v1/firewalls/{firewallId} | Get specific firewall by its id
[**retrieve_firewall_list**](FirewallsApi.md#retrieve_firewall_list) | **GET** /v1/firewalls | List firewalls
[**set_default_firewall**](FirewallsApi.md#set_default_firewall) | **PUT** /v1/firewalls/{firewallId}/default | Set specific firewall to be default


# **create_firewall**
> CreateFirewallResponse create_firewall(x_request_id, create_firewall_request)

Create a new firewall

Create a firewall for you account with the provided setup.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
from pfruck_contabo.model.create_firewall_request import CreateFirewallRequest
from pfruck_contabo.model.create_firewall_response import CreateFirewallResponse
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_firewall_request = CreateFirewallRequest(
        name="My Firewall",
        description="This is the firewall for instance 1, 2, 3.",
        status="active",
        rules=Rules(
            inbound=[
                InboundRule(
                    protocol="tcp",
                    src_ports=[
                        "["80", "80-90"]",
                    ],
                    src_cidr=SrcCidr(
                        ipv4=["192.168.0.1/24"],
                        ipv6=["1:2:3:4:5:6:7:8::64"],
                    ),
                    action="accept",
                    status="active",
                ),
            ],
        ),
    ) # CreateFirewallRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new firewall
        api_response = api_instance.create_firewall(x_request_id, create_firewall_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->create_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new firewall
        api_response = api_instance.create_firewall(x_request_id, create_firewall_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->create_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **create_firewall_request** | [**CreateFirewallRequest**](CreateFirewallRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CreateFirewallResponse**](CreateFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard firewall attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall**
> delete_firewall(x_request_id, firewall_id)

Delete existing Firewall by id

Delete existing Firewall by id. A firewall cannot be deleted if there are instances attached to it.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = "b943b25a-c8b5-4570-9135-4bbaa7615b81" # str | The identifier of the firewall
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete existing Firewall by id
        api_instance.delete_firewall(x_request_id, firewall_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete existing Firewall by id
        api_instance.delete_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->delete_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **firewall_id** | **str**| The identifier of the firewall |
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

# **patch_firewall**
> PatchFirewallResponse patch_firewall(x_request_id, firewall_id, patch_firewall_request)

Update a Firewall by id

Update a Firewall by id in your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
from pfruck_contabo.model.patch_firewall_response import PatchFirewallResponse
from pfruck_contabo.model.patch_firewall_request import PatchFirewallRequest
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = "b943b25a-c8b5-4570-9135-4bbaa7615b81" # str | The identifier of the firewall
    patch_firewall_request = PatchFirewallRequest(
        name="My Firewall",
        status="active",
        description="Firewall description",
    ) # PatchFirewallRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Firewall by id
        api_response = api_instance.patch_firewall(x_request_id, firewall_id, patch_firewall_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->patch_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Firewall by id
        api_response = api_instance.patch_firewall(x_request_id, firewall_id, patch_firewall_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->patch_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **firewall_id** | **str**| The identifier of the firewall |
 **patch_firewall_request** | [**PatchFirewallRequest**](PatchFirewallRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**PatchFirewallResponse**](PatchFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard Firewall attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_firewall**
> PutFirewallResponse put_firewall(x_request_id, firewall_id, put_firewall_request)

Update specific firewall rules

Set rules for a specific firewall

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
from pfruck_contabo.model.put_firewall_request import PutFirewallRequest
from pfruck_contabo.model.put_firewall_response import PutFirewallResponse
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = "b943b25a-c8b5-4570-9135-4bbaa7615b81" # str | The identifier of the firewall
    put_firewall_request = PutFirewallRequest(
        rules=Rules(
            inbound=[
                InboundRule(
                    protocol="tcp",
                    src_ports=[
                        "["80", "80-90"]",
                    ],
                    src_cidr=SrcCidr(
                        ipv4=["192.168.0.1/24"],
                        ipv6=["1:2:3:4:5:6:7:8::64"],
                    ),
                    action="accept",
                    status="active",
                ),
            ],
        ),
    ) # PutFirewallRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update specific firewall rules
        api_response = api_instance.put_firewall(x_request_id, firewall_id, put_firewall_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->put_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update specific firewall rules
        api_response = api_instance.put_firewall(x_request_id, firewall_id, put_firewall_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->put_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **firewall_id** | **str**| The identifier of the firewall |
 **put_firewall_request** | [**PutFirewallRequest**](PutFirewallRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**PutFirewallResponse**](PutFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a details of a firewall. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_firewall**
> FindFirewallResponse retrieve_firewall(x_request_id, firewall_id)

Get specific firewall by its id

Get data for a specific firewall on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
from pfruck_contabo.model.find_firewall_response import FindFirewallResponse
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = "b943b25a-c8b5-4570-9135-4bbaa7615b81" # str | The identifier of the firewall
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific firewall by its id
        api_response = api_instance.retrieve_firewall(x_request_id, firewall_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->retrieve_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific firewall by its id
        api_response = api_instance.retrieve_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->retrieve_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **firewall_id** | **str**| The identifier of the firewall |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindFirewallResponse**](FindFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a paginated list of Firewalls. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_firewall_list**
> ListFirewallResponse retrieve_firewall_list(x_request_id)

List firewalls

List and filter all Firewalls in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
from pfruck_contabo.model.list_firewall_response import ListFirewallResponse
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = "myPrivateNetwork" # str | The name of the Firewall (optional)

    # example passing only required values which don't have defaults set
    try:
        # List firewalls
        api_response = api_instance.retrieve_firewall_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->retrieve_firewall_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List firewalls
        api_response = api_instance.retrieve_firewall_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->retrieve_firewall_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **name** | **str**| The name of the Firewall | [optional]

### Return type

[**ListFirewallResponse**](ListFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a paginated list of Firewalls. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_firewall**
> SetDefaultFirewallResponse set_default_firewall(x_request_id, firewall_id)

Set specific firewall to be default

Set a specific firewall to be the default

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import firewalls_api
from pfruck_contabo.model.set_default_firewall_response import SetDefaultFirewallResponse
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
    api_instance = firewalls_api.FirewallsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = "b943b25a-c8b5-4570-9135-4bbaa7615b81" # str | The identifier of the firewall
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set specific firewall to be default
        api_response = api_instance.set_default_firewall(x_request_id, firewall_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->set_default_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set specific firewall to be default
        api_response = api_instance.set_default_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling FirewallsApi->set_default_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **firewall_id** | **str**| The identifier of the firewall |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**SetDefaultFirewallResponse**](SetDefaultFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a details of a firewall. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

