# pfruck_contabo.InstancesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_instance**](InstancesApi.md#cancel_instance) | **POST** /v1/compute/instances/{instanceId}/cancel | Cancel specific instance by id
[**check_set_new_host**](InstancesApi.md#check_set_new_host) | **GET** /v1/compute/instances/{instanceId}/regionChange/check | Check if the instance can be moved to another host
[**create_instance**](InstancesApi.md#create_instance) | **POST** /v1/compute/instances | Create a new instance
[**patch_instance**](InstancesApi.md#patch_instance) | **PATCH** /v1/compute/instances/{instanceId} | Update specific instance
[**reinstall_instance**](InstancesApi.md#reinstall_instance) | **PUT** /v1/compute/instances/{instanceId} | Reinstall specific instance
[**request_region_change**](InstancesApi.md#request_region_change) | **POST** /v1/compute/instances/{instanceId}/regionChange | Request instance region change
[**retrieve_available_instance_products**](InstancesApi.md#retrieve_available_instance_products) | **GET** /v1/compute/instances/{instanceId}/products/available | Get the available products of a specific instance
[**retrieve_instance**](InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
[**retrieve_instances_list**](InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances
[**upgrade_instance**](InstancesApi.md#upgrade_instance) | **POST** /v1/compute/instances/{instanceId}/upgrade | Upgrading instance capabilities


# **cancel_instance**
> CancelInstanceResponse cancel_instance(x_request_id, instance_id, cancel_instance_request, x_trace_id=x_trace_id)

Cancel specific instance by id

Your are free to cancel a previously created instance at any time.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_instance_request import CancelInstanceRequest
from pfruck_contabo.models.cancel_instance_response import CancelInstanceResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    cancel_instance_request = pfruck_contabo.CancelInstanceRequest() # CancelInstanceRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Cancel specific instance by id
        api_response = api_instance.cancel_instance(x_request_id, instance_id, cancel_instance_request, x_trace_id=x_trace_id)
        print("The response of InstancesApi->cancel_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->cancel_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **cancel_instance_request** | [**CancelInstanceRequest**](CancelInstanceRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CancelInstanceResponse**](CancelInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard custom image attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_set_new_host**
> check_set_new_host(x_request_id, instance_id, x_trace_id=x_trace_id)

Check if the instance can be moved to another host

Verifies preconditions with CMS before relocating the instance from its current host. Returns no content when the check succeeds. When CMS responds with an error list, returns that payload with the same HTTP status as CMS.

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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Check if the instance can be moved to another host
        api_instance.check_set_new_host(x_request_id, instance_id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling InstancesApi->check_set_new_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The instance may be moved; CMS returned success. |  -  |
**400** | CMS rejected the check; response lists error codes. Actual status matches CMS (4xx). |  -  |
**500** | CMS or upstream failure with an errors list in the body when applicable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_instance**
> CreateInstanceResponse create_instance(x_request_id, create_instance_request, x_trace_id=x_trace_id)

Create a new instance

Create a new instance for your account with the provided parameters.         <table>           <tr><th>ProductId</th><th>Product</th><th>Disk Size</th></tr>           <tr><td>V153</td><td>Cloud VPS 4</td><td>100 GB SSD</td></tr>           <tr><td>V154</td><td>Cloud VPS 6</td><td>200 GB SSD</td></tr>           <tr><td>V155</td><td>Cloud VPS 8</td><td>300 GB SSD</td></tr>           <tr><td>V156</td><td>Cloud VPS 12</td><td>400 GB SSD</td></tr>           <tr><td>V157</td><td>Cloud VPS 16</td><td>500 GB SSD</td></tr>           <tr><td>V158</td><td>Cloud VPS 18</td><td>600 GB SSD</td></tr>           <tr><td>V159</td><td>Cloud VPS Plus 4</td><td>150 GB NVMe</td></tr>           <tr><td>V160</td><td>Cloud VPS Plus 6</td><td>300 GB NVMe</td></tr>           <tr><td>V161</td><td>Cloud VPS Plus 8</td><td>450 GB NVMe</td></tr>           <tr><td>V162</td><td>Cloud VPS Plus 12</td><td>600 GB NVMe</td></tr>           <tr><td>V163</td><td>Cloud VPS Plus 16</td><td>750 GB NVMe</td></tr>           <tr><td>V164</td><td>Cloud VPS Plus 18</td><td>900 GB NVMe</td></tr>           <tr><td>V93</td><td>VPS 10 Storage</td><td>300 GB SSD</td></tr>          <tr><td>V96</td><td>VPS 20 Storage</td><td>400 GB SSD</td></tr>           <tr><td>V99</td><td>VPS 30 Storage</td><td>1000 GB SSD</td></tr>           <tr><td>V102</td><td>VPS 40 Storage</td><td>1200 GB SSD</td></tr>           <tr><td>V105</td><td>VPS 50 Storage</td><td>1400 GB SSD</td></tr>           <tr><td>V8</td><td>VDS S</td><td>180 GB NVMe</td></tr>           <tr><td>V9</td><td>VDS M</td><td>240 GB NVMe</td></tr>           <tr><td>V10</td><td>VDS L</td><td>360 GB NVMe</td></tr>           <tr><td>V11</td><td>VDS XL</td><td>480 GB NVMe</td></tr>           <tr><td>V16</td><td>VDS XXL</td><td>720 GB NVMe</td></tr>           </table>

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.create_instance_request import CreateInstanceRequest
from pfruck_contabo.models.create_instance_response import CreateInstanceResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_instance_request = pfruck_contabo.CreateInstanceRequest() # CreateInstanceRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create a new instance
        api_response = api_instance.create_instance(x_request_id, create_instance_request, x_trace_id=x_trace_id)
        print("The response of InstancesApi->create_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->create_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **create_instance_request** | [**CreateInstanceRequest**](CreateInstanceRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateInstanceResponse**](CreateInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard instance attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_instance**
> PatchInstanceResponse patch_instance(x_request_id, instance_id, patch_instance_request, x_trace_id=x_trace_id)

Update specific instance

Update specific instance by instanceId.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.patch_instance_request import PatchInstanceRequest
from pfruck_contabo.models.patch_instance_response import PatchInstanceResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    patch_instance_request = pfruck_contabo.PatchInstanceRequest() # PatchInstanceRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update specific instance
        api_response = api_instance.patch_instance(x_request_id, instance_id, patch_instance_request, x_trace_id=x_trace_id)
        print("The response of InstancesApi->patch_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->patch_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **patch_instance_request** | [**PatchInstanceRequest**](PatchInstanceRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**PatchInstanceResponse**](PatchInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains instanceId and createdDate. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reinstall_instance**
> ReinstallInstanceResponse reinstall_instance(x_request_id, instance_id, reinstall_instance_request, x_trace_id=x_trace_id)

Reinstall specific instance

You can reinstall a specific instance with a new image and optionally add ssh keys, a root password or cloud-init.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.reinstall_instance_request import ReinstallInstanceRequest
from pfruck_contabo.models.reinstall_instance_response import ReinstallInstanceResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    reinstall_instance_request = pfruck_contabo.ReinstallInstanceRequest() # ReinstallInstanceRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Reinstall specific instance
        api_response = api_instance.reinstall_instance(x_request_id, instance_id, reinstall_instance_request, x_trace_id=x_trace_id)
        print("The response of InstancesApi->reinstall_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->reinstall_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **reinstall_instance_request** | [**ReinstallInstanceRequest**](ReinstallInstanceRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ReinstallInstanceResponse**](ReinstallInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains instanceId and createdDate. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_region_change**
> InstanceRegionChangeResponse request_region_change(x_request_id, instance_id, region_change_request, x_trace_id=x_trace_id)

Request instance region change

Starts a region change for the instance via CMS. Returns the support ticket number when the operation was accepted.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.instance_region_change_response import InstanceRegionChangeResponse
from pfruck_contabo.models.region_change_request import RegionChangeRequest
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    region_change_request = pfruck_contabo.RegionChangeRequest() # RegionChangeRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Request instance region change
        api_response = api_instance.request_region_change(x_request_id, instance_id, region_change_request, x_trace_id=x_trace_id)
        print("The response of InstancesApi->request_region_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->request_region_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **region_change_request** | [**RegionChangeRequest**](RegionChangeRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**InstanceRegionChangeResponse**](InstanceRegionChangeResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CMS accepted the region change request and returned a ticket number. |  -  |
**400** | CMS rejected the request; response lists error codes. |  -  |
**500** | CMS or upstream error; may include error codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_available_instance_products**
> ListInstanceProductsResponse retrieve_available_instance_products(x_request_id, instance_id, x_trace_id=x_trace_id)

Get the available products of a specific instance

Get all products the instance can be upgraded to, excluding the currently assigned one. Use the `offerId` of the desired product to submit the upgrade.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_instance_products_response import ListInstanceProductsResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get the available products of a specific instance
        api_response = api_instance.retrieve_available_instance_products(x_request_id, instance_id, x_trace_id=x_trace_id)
        print("The response of InstancesApi->retrieve_available_instance_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->retrieve_available_instance_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ListInstanceProductsResponse**](ListInstanceProductsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the products available for the instance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_instance**
> FindInstanceResponse retrieve_instance(x_request_id, instance_id, x_trace_id=x_trace_id)

Get specific instance by id

Get attributes values to a specific instance on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_instance_response import FindInstanceResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get specific instance by id
        api_response = api_instance.retrieve_instance(x_request_id, instance_id, x_trace_id=x_trace_id)
        print("The response of InstancesApi->retrieve_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->retrieve_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindInstanceResponse**](FindInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard instance attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_instances_list**
> ListInstancesResponse retrieve_instances_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, display_name=display_name, data_center=data_center, region=region, instance_id=instance_id, instance_ids=instance_ids, status=status, product_ids=product_ids, add_on_ids=add_on_ids, product_types=product_types, ip_config=ip_config, suspended=suspended, search=search, customer_id=customer_id, tenant_id=tenant_id)

List instances

List and filter all instances in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_instances_response import ListInstancesResponse
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = 'vmd12345' # str | The name of the instance (optional)
    display_name = 'myTestInstance' # str | The display name of the instance (optional)
    data_center = 'European Union 1' # str | The data center of the instance (optional)
    region = 'EU' # str | The Region of the instance (optional)
    instance_id = 100 # int | The identifier of the instance (deprecated) (optional)
    instance_ids = '100, 101, 102' # str | Comma separated instances identifiers (optional)
    status = 'provisioning,installing' # str | The status of the instance (optional)
    product_ids = 'V68,V77' # str | Identifiers of the instance products (optional)
    add_on_ids = '1044,827' # str | Identifiers of Addons the instances have (optional)
    product_types = 'ssd, hdd, nvme' # str | Comma separated instance's category depending on Product Id (optional)
    ip_config = true # bool | Filter instances that have an ip config (optional)
    suspended = false # bool | Filter instances by suspension state. When set to false, suspended instances are excluded from the response. Any other value returns all instances (default behavior). (optional)
    search = 'vmd12345' # str | Full text search when listing the instances. Can be searched by `name`, `displayName`, `ipAddress` (optional)
    customer_id = '22223' # str | Filter by customer ID (optional)
    tenant_id = 'DE' # str | Filter by tenant ID (optional)

    try:
        # List instances
        api_response = api_instance.retrieve_instances_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, display_name=display_name, data_center=data_center, region=region, instance_id=instance_id, instance_ids=instance_ids, status=status, product_ids=product_ids, add_on_ids=add_on_ids, product_types=product_types, ip_config=ip_config, suspended=suspended, search=search, customer_id=customer_id, tenant_id=tenant_id)
        print("The response of InstancesApi->retrieve_instances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->retrieve_instances_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of the instance | [optional] 
 **display_name** | **str**| The display name of the instance | [optional] 
 **data_center** | **str**| The data center of the instance | [optional] 
 **region** | **str**| The Region of the instance | [optional] 
 **instance_id** | **int**| The identifier of the instance (deprecated) | [optional] 
 **instance_ids** | **str**| Comma separated instances identifiers | [optional] 
 **status** | **str**| The status of the instance | [optional] 
 **product_ids** | **str**| Identifiers of the instance products | [optional] 
 **add_on_ids** | **str**| Identifiers of Addons the instances have | [optional] 
 **product_types** | **str**| Comma separated instance&#39;s category depending on Product Id | [optional] 
 **ip_config** | **bool**| Filter instances that have an ip config | [optional] 
 **suspended** | **bool**| Filter instances by suspension state. When set to false, suspended instances are excluded from the response. Any other value returns all instances (default behavior). | [optional] 
 **search** | **str**| Full text search when listing the instances. Can be searched by &#x60;name&#x60;, &#x60;displayName&#x60;, &#x60;ipAddress&#x60; | [optional] 
 **customer_id** | **str**| Filter by customer ID | [optional] 
 **tenant_id** | **str**| Filter by tenant ID | [optional] 

### Return type

[**ListInstancesResponse**](ListInstancesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of instances. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_instance**
> PatchInstanceResponse upgrade_instance(x_request_id, instance_id, upgrade_instance_request, x_trace_id=x_trace_id)

Upgrading instance capabilities

In order to enhance your instance with additional features you can purchase add-ons.   Currently only firewalling and private network addon is allowed.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.patch_instance_response import PatchInstanceResponse
from pfruck_contabo.models.upgrade_instance_request import UpgradeInstanceRequest
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
    api_instance = pfruck_contabo.InstancesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    upgrade_instance_request = pfruck_contabo.UpgradeInstanceRequest() # UpgradeInstanceRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Upgrading instance capabilities
        api_response = api_instance.upgrade_instance(x_request_id, instance_id, upgrade_instance_request, x_trace_id=x_trace_id)
        print("The response of InstancesApi->upgrade_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->upgrade_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **upgrade_instance_request** | [**UpgradeInstanceRequest**](UpgradeInstanceRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**PatchInstanceResponse**](PatchInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard instance attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

