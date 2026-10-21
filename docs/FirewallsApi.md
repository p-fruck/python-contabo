# pfruck_contabo.FirewallsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_instance_firewall**](FirewallsApi.md#assign_instance_firewall) | **POST** /v1/firewalls/{firewallId}/instances/{instanceId} | Add instance to a firewall
[**create_firewall**](FirewallsApi.md#create_firewall) | **POST** /v1/firewalls | Create a new firewall definition
[**delete_firewall**](FirewallsApi.md#delete_firewall) | **DELETE** /v1/firewalls/{firewallId} | Delete existing firewall by id
[**patch_firewall**](FirewallsApi.md#patch_firewall) | **PATCH** /v1/firewalls/{firewallId} | Update a firewall by id
[**put_firewall**](FirewallsApi.md#put_firewall) | **PUT** /v1/firewalls/{firewallId} | Update specific firewall rules
[**retrieve_firewall**](FirewallsApi.md#retrieve_firewall) | **GET** /v1/firewalls/{firewallId} | Get specific firewall by its id
[**retrieve_firewall_list**](FirewallsApi.md#retrieve_firewall_list) | **GET** /v1/firewalls | List all firewalls
[**retrieve_preset_rules**](FirewallsApi.md#retrieve_preset_rules) | **GET** /v1/firewalls/preset-rules | Get all preset rules
[**unassign_instance_firewall**](FirewallsApi.md#unassign_instance_firewall) | **DELETE** /v1/firewalls/{firewallId}/instances/{instanceId} | Remove instance from a firewall


# **assign_instance_firewall**
> AssignInstanceFirewallResponse assign_instance_firewall(x_request_id, firewall_id, instance_id, x_trace_id=x_trace_id)

Add instance to a firewall

Add a specific instance to a firewall

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.assign_instance_firewall_response import AssignInstanceFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81' # str | The identifier of the firewall
    instance_id = 100 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Add instance to a firewall
        api_response = api_instance.assign_instance_firewall(x_request_id, firewall_id, instance_id, x_trace_id=x_trace_id)
        print("The response of FirewallsApi->assign_instance_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->assign_instance_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **firewall_id** | **str**| The identifier of the firewall | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**AssignInstanceFirewallResponse**](AssignInstanceFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instance will be added to the firewall |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall**
> CreateFirewallResponse create_firewall(x_request_id, create_firewall_request, x_trace_id=x_trace_id)

Create a new firewall definition

Create a new firewall definition by specifying its name and a set of rules. The status of the firewall determines whether the rules are active or not.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.create_firewall_request import CreateFirewallRequest
from pfruck_contabo.models.create_firewall_response import CreateFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_firewall_request = pfruck_contabo.CreateFirewallRequest() # CreateFirewallRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create a new firewall definition
        api_response = api_instance.create_firewall(x_request_id, create_firewall_request, x_trace_id=x_trace_id)
        print("The response of FirewallsApi->create_firewall:\n")
        pprint(api_response)
    except Exception as e:
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
> delete_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id)

Delete existing firewall by id

Delete existing firewall by id. A firewall cannot be deleted if there are instances attached to it.

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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81' # str | The identifier of the firewall
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Delete existing firewall by id
        api_instance.delete_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id)
    except Exception as e:
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
> PatchFirewallResponse patch_firewall(x_request_id, firewall_id, patch_firewall_request, x_trace_id=x_trace_id)

Update a firewall by id

Update a firewall by id in your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.patch_firewall_request import PatchFirewallRequest
from pfruck_contabo.models.patch_firewall_response import PatchFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81' # str | The identifier of the firewall
    patch_firewall_request = pfruck_contabo.PatchFirewallRequest() # PatchFirewallRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update a firewall by id
        api_response = api_instance.patch_firewall(x_request_id, firewall_id, patch_firewall_request, x_trace_id=x_trace_id)
        print("The response of FirewallsApi->patch_firewall:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | The response will be a JSON object and contains standard firewall attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_firewall**
> PutFirewallResponse put_firewall(x_request_id, firewall_id, put_firewall_request, x_trace_id=x_trace_id)

Update specific firewall rules

Set rules for a specific firewall. Currently only inbound rules are allowed to be configured.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.put_firewall_request import PutFirewallRequest
from pfruck_contabo.models.put_firewall_response import PutFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81' # str | The identifier of the firewall
    put_firewall_request = pfruck_contabo.PutFirewallRequest() # PutFirewallRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update specific firewall rules
        api_response = api_instance.put_firewall(x_request_id, firewall_id, put_firewall_request, x_trace_id=x_trace_id)
        print("The response of FirewallsApi->put_firewall:\n")
        pprint(api_response)
    except Exception as e:
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
> FindFirewallResponse retrieve_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, instance_ids=instance_ids)

Get specific firewall by its id

Get data for a specific firewall on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_firewall_response import FindFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81' # str | The identifier of the firewall
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = 'My Firewall' # str | The name of the firewall (optional)
    instance_ids = '12345,67890' # str | Comma separated instance IDs. (optional)

    try:
        # Get specific firewall by its id
        api_response = api_instance.retrieve_firewall(x_request_id, firewall_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, instance_ids=instance_ids)
        print("The response of FirewallsApi->retrieve_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->retrieve_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **firewall_id** | **str**| The identifier of the firewall | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of the firewall | [optional] 
 **instance_ids** | **str**| Comma separated instance IDs. | [optional] 

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
> ListFirewallResponse retrieve_firewall_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, instance_ids=instance_ids)

List all firewalls

List and filter all firewalls on your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_firewall_response import ListFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = 'My Firewall' # str | The name of the firewall (optional)
    instance_ids = '12345,67890' # str | Comma separated instance IDs. (optional)

    try:
        # List all firewalls
        api_response = api_instance.retrieve_firewall_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, instance_ids=instance_ids)
        print("The response of FirewallsApi->retrieve_firewall_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->retrieve_firewall_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of the firewall | [optional] 
 **instance_ids** | **str**| Comma separated instance IDs. | [optional] 

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

# **retrieve_preset_rules**
> ListPresetRulesResponse retrieve_preset_rules(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name)

Get all preset rules

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_preset_rules_response import ListPresetRulesResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = 'SSH' # str | The name of preset rule (optional)

    try:
        # Get all preset rules
        api_response = api_instance.retrieve_preset_rules(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name)
        print("The response of FirewallsApi->retrieve_preset_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->retrieve_preset_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of preset rule | [optional] 

### Return type

[**ListPresetRulesResponse**](ListPresetRulesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a list of preset rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_instance_firewall**
> UnassignInstanceFirewallResponse unassign_instance_firewall(x_request_id, firewall_id, instance_id, x_trace_id=x_trace_id)

Remove instance from a firewall

Remove a specific instance from a firewall

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.unassign_instance_firewall_response import UnassignInstanceFirewallResponse
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
    api_instance = pfruck_contabo.FirewallsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    firewall_id = 'b943b25a-c8b5-4570-9135-4bbaa7615b81' # str | The identifier of the firewall
    instance_id = 100 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Remove instance from a firewall
        api_response = api_instance.unassign_instance_firewall(x_request_id, firewall_id, instance_id, x_trace_id=x_trace_id)
        print("The response of FirewallsApi->unassign_instance_firewall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallsApi->unassign_instance_firewall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **firewall_id** | **str**| The identifier of the firewall | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UnassignInstanceFirewallResponse**](UnassignInstanceFirewallResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instance will be removed from the firewall |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

