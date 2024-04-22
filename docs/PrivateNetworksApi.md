# pfruck_contabo.PrivateNetworksApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_instance_private_network**](PrivateNetworksApi.md#assign_instance_private_network) | **POST** /v1/private-networks/{privateNetworkId}/instances/{instanceId} | Add instance to a Private Network
[**create_private_network**](PrivateNetworksApi.md#create_private_network) | **POST** /v1/private-networks | Create a new Private Network
[**delete_private_network**](PrivateNetworksApi.md#delete_private_network) | **DELETE** /v1/private-networks/{privateNetworkId} | Delete existing Private Network by id
[**patch_private_network**](PrivateNetworksApi.md#patch_private_network) | **PATCH** /v1/private-networks/{privateNetworkId} | Update a Private Network by id
[**retrieve_private_network**](PrivateNetworksApi.md#retrieve_private_network) | **GET** /v1/private-networks/{privateNetworkId} | Get specific Private Network by id
[**retrieve_private_network_list**](PrivateNetworksApi.md#retrieve_private_network_list) | **GET** /v1/private-networks | List Private Networks
[**unassign_instance_private_network**](PrivateNetworksApi.md#unassign_instance_private_network) | **DELETE** /v1/private-networks/{privateNetworkId}/instances/{instanceId} | Remove instance from a Private Network


# **assign_instance_private_network**
> AssignInstancePrivateNetworkResponse assign_instance_private_network(x_request_id, private_network_id, instance_id, x_trace_id=x_trace_id)

Add instance to a Private Network

Add a specific instance to a Private Network

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.assign_instance_private_network_response import AssignInstancePrivateNetworkResponse
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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the Private Network
    instance_id = 100 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Add instance to a Private Network
        api_response = api_instance.assign_instance_private_network(x_request_id, private_network_id, instance_id, x_trace_id=x_trace_id)
        print("The response of PrivateNetworksApi->assign_instance_private_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->assign_instance_private_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **private_network_id** | **int**| The identifier of the Private Network | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**AssignInstancePrivateNetworkResponse**](AssignInstancePrivateNetworkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instance will be added to the Private Network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_private_network**
> CreatePrivateNetworkResponse create_private_network(x_request_id, create_private_network_request, x_trace_id=x_trace_id)

Create a new Private Network

Create a new Private Network in your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.create_private_network_request import CreatePrivateNetworkRequest
from pfruck_contabo.models.create_private_network_response import CreatePrivateNetworkResponse
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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_private_network_request = pfruck_contabo.CreatePrivateNetworkRequest() # CreatePrivateNetworkRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create a new Private Network
        api_response = api_instance.create_private_network(x_request_id, create_private_network_request, x_trace_id=x_trace_id)
        print("The response of PrivateNetworksApi->create_private_network:\n")
        pprint(api_response)
    except Exception as e:
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
**201** | The response will be a JSON object and contains standard Private Network attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_private_network**
> delete_private_network(x_request_id, private_network_id, x_trace_id=x_trace_id)

Delete existing Private Network by id

Delete existing Virtual Private Cloud by id and automatically unassign all instances from it

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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the Private Network
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Delete existing Private Network by id
        api_instance.delete_private_network(x_request_id, private_network_id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->delete_private_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **private_network_id** | **int**| The identifier of the Private Network | 
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

# **patch_private_network**
> PatchPrivateNetworkResponse patch_private_network(x_request_id, private_network_id, patch_private_network_request, x_trace_id=x_trace_id)

Update a Private Network by id

Update a Private Network by id in your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.patch_private_network_request import PatchPrivateNetworkRequest
from pfruck_contabo.models.patch_private_network_response import PatchPrivateNetworkResponse
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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the Private Network
    patch_private_network_request = pfruck_contabo.PatchPrivateNetworkRequest() # PatchPrivateNetworkRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update a Private Network by id
        api_response = api_instance.patch_private_network(x_request_id, private_network_id, patch_private_network_request, x_trace_id=x_trace_id)
        print("The response of PrivateNetworksApi->patch_private_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->patch_private_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **private_network_id** | **int**| The identifier of the Private Network | 
 **patch_private_network_request** | [**PatchPrivateNetworkRequest**](PatchPrivateNetworkRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**PatchPrivateNetworkResponse**](PatchPrivateNetworkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard Private Network attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_private_network**
> FindPrivateNetworkResponse retrieve_private_network(x_request_id, private_network_id, x_trace_id=x_trace_id)

Get specific Private Network by id

Get attributes values to a specific Private Network on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_private_network_response import FindPrivateNetworkResponse
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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 12345 # int | The identifier of the Private Network
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get specific Private Network by id
        api_response = api_instance.retrieve_private_network(x_request_id, private_network_id, x_trace_id=x_trace_id)
        print("The response of PrivateNetworksApi->retrieve_private_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->retrieve_private_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **private_network_id** | **int**| The identifier of the Private Network | 
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
**200** | The response will be a JSON object and contains standard Private Network attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_private_network_list**
> ListPrivateNetworkResponse retrieve_private_network_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, instance_ids=instance_ids, region=region, data_center=data_center)

List Private Networks

List and filter all Private Networks in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_private_network_response import ListPrivateNetworkResponse
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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = 'myPrivateNetwork' # str | The name of the Private Network (optional)
    instance_ids = '100, 101, 102' # str | Comma separated instances identifiers (optional)
    region = 'EU' # str | The slug of the region where your Private Network is located (optional)
    data_center = 'European Union 1' # str | The data center where your Private Network is located (optional)

    try:
        # List Private Networks
        api_response = api_instance.retrieve_private_network_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, instance_ids=instance_ids, region=region, data_center=data_center)
        print("The response of PrivateNetworksApi->retrieve_private_network_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->retrieve_private_network_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of the Private Network | [optional] 
 **instance_ids** | **str**| Comma separated instances identifiers | [optional] 
 **region** | **str**| The slug of the region where your Private Network is located | [optional] 
 **data_center** | **str**| The data center where your Private Network is located | [optional] 

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
**200** | The response will be a JSON object and contains a paginated list of Private Networks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_instance_private_network**
> UnassignInstancePrivateNetworkResponse unassign_instance_private_network(x_request_id, private_network_id, instance_id, x_trace_id=x_trace_id)

Remove instance from a Private Network

Remove a specific instance from a Private Network

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.unassign_instance_private_network_response import UnassignInstancePrivateNetworkResponse
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
    api_instance = pfruck_contabo.PrivateNetworksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    private_network_id = 100 # int | The identifier of the Private Network
    instance_id = 100 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Remove instance from a Private Network
        api_response = api_instance.unassign_instance_private_network(x_request_id, private_network_id, instance_id, x_trace_id=x_trace_id)
        print("The response of PrivateNetworksApi->unassign_instance_private_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->unassign_instance_private_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **private_network_id** | **int**| The identifier of the Private Network | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UnassignInstancePrivateNetworkResponse**](UnassignInstancePrivateNetworkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instance will be removed from the Private Network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

