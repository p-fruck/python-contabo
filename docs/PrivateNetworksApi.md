# pfruck_contabo.PrivateNetworksApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_instance_private_network**](PrivateNetworksApi.md#assign_instance_private_network) | **POST** /v1/virtual-private-cloud/{privateNetworkId}/instances/{instanceId} | Add instance to a private network
[**create_private_network**](PrivateNetworksApi.md#create_private_network) | **POST** /v1/virtual-private-cloud | Create a new private network
[**retrieve_private_network**](PrivateNetworksApi.md#retrieve_private_network) | **GET** /v1/virtual-private-cloud/{privateNetworkId} | Get specific private network by id
[**retrieve_private_network_list**](PrivateNetworksApi.md#retrieve_private_network_list) | **GET** /v1/virtual-private-cloud | List private networks
[**unassign_instance_private_network**](PrivateNetworksApi.md#unassign_instance_private_network) | **DELETE** /v1/virtual-private-cloud/{privateNetworkId}/instances/{instanceId} | Remove instance from a private network


# **assign_instance_private_network**
> AssignInstancePrivateNetworkReponse assign_instance_private_network(x_request_id, private_network_id, instance_id)

Add instance to a private network

Add a specific instance to a private network

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import private_networks_api
from pfruck_contabo.model.assign_instance_private_network_reponse import AssignInstancePrivateNetworkReponse
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
    api_instance = private_networks_api.PrivateNetworksApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the privateNetwork
    instance_id = 100 # int | The identifier of the instance
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add instance to a private network
        api_response = api_instance.assign_instance_private_network(x_request_id, private_network_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->assign_instance_private_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add instance to a private network
        api_response = api_instance.assign_instance_private_network(x_request_id, private_network_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->assign_instance_private_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **private_network_id** | **int**| The identifier of the privateNetwork |
 **instance_id** | **int**| The identifier of the instance |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**AssignInstancePrivateNetworkReponse**](AssignInstancePrivateNetworkReponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instance will be added to the private network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_private_network**
> CreatePrivateNetworkResponse create_private_network(x_request_id, create_private_network_request)

Create a new private network

Create a new private network in your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import private_networks_api
from pfruck_contabo.model.create_private_network_request import CreatePrivateNetworkRequest
from pfruck_contabo.model.create_private_network_response import CreatePrivateNetworkResponse
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
    api_instance = private_networks_api.PrivateNetworksApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_private_network_request = CreatePrivateNetworkRequest(
        region="EU",
        name="VPN",
        description="VPN Description",
    ) # CreatePrivateNetworkRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new private network
        api_response = api_instance.create_private_network(x_request_id, create_private_network_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->create_private_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new private network
        api_response = api_instance.create_private_network(x_request_id, create_private_network_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->create_private_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **create_private_network_request** | [**CreatePrivateNetworkRequest**](CreatePrivateNetworkRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CreatePrivateNetworkResponse**](CreatePrivateNetworkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard private network attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_private_network**
> FindPrivateNetworkResponse retrieve_private_network(x_request_id, private_network_id)

Get specific private network by id

Get attributes values to a specific private network on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import private_networks_api
from pfruck_contabo.model.find_private_network_response import FindPrivateNetworkResponse
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
    api_instance = private_networks_api.PrivateNetworksApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the private network
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific private network by id
        api_response = api_instance.retrieve_private_network(x_request_id, private_network_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->retrieve_private_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific private network by id
        api_response = api_instance.retrieve_private_network(x_request_id, private_network_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->retrieve_private_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **private_network_id** | **int**| The identifier of the private network |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindPrivateNetworkResponse**](FindPrivateNetworkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard private network attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_private_network_list**
> ListPrivateNetworkResponse retrieve_private_network_list(x_request_id)

List private networks

List and filter all private networks in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import private_networks_api
from pfruck_contabo.model.list_private_network_response import ListPrivateNetworkResponse
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
    api_instance = private_networks_api.PrivateNetworksApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = "VPN" # str | The name of the virtual private network (optional)

    # example passing only required values which don't have defaults set
    try:
        # List private networks
        api_response = api_instance.retrieve_private_network_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->retrieve_private_network_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List private networks
        api_response = api_instance.retrieve_private_network_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->retrieve_private_network_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **name** | **str**| The name of the virtual private network | [optional]

### Return type

[**ListPrivateNetworkResponse**](ListPrivateNetworkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of private networks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_instance_private_network**
> UnassignInstancePrivateNetworkReponse unassign_instance_private_network(x_request_id, private_network_id, instance_id)

Remove instance from a private network

Remove a specific instance from a private network

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import private_networks_api
from pfruck_contabo.model.unassign_instance_private_network_reponse import UnassignInstancePrivateNetworkReponse
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
    api_instance = private_networks_api.PrivateNetworksApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the privateNetwork
    instance_id = 100 # int | The identifier of the instance
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove instance from a private network
        api_response = api_instance.unassign_instance_private_network(x_request_id, private_network_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->unassign_instance_private_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove instance from a private network
        api_response = api_instance.unassign_instance_private_network(x_request_id, private_network_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling PrivateNetworksApi->unassign_instance_private_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **private_network_id** | **int**| The identifier of the privateNetwork |
 **instance_id** | **int**| The identifier of the instance |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**UnassignInstancePrivateNetworkReponse**](UnassignInstancePrivateNetworkReponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instance will be removed from the private network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

