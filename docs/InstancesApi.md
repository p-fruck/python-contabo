# pfruck_contabo.InstancesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_instance**](InstancesApi.md#cancel_instance) | **POST** /v1/compute/instances/{instanceId}/cancel | Cancel specific instance by id
[**create_instance**](InstancesApi.md#create_instance) | **POST** /v1/compute/instances | Create a new instance
[**patch_instance**](InstancesApi.md#patch_instance) | **PATCH** /v1/compute/instances/{instanceId} | Update specific instance
[**reinstall_instance**](InstancesApi.md#reinstall_instance) | **PUT** /v1/compute/instances/{instanceId} | Reinstall specific instance
[**retrieve_instance**](InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
[**retrieve_instances_list**](InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances
[**upgrade_instance**](InstancesApi.md#upgrade_instance) | **POST** /v1/compute/instances/{instanceId}/upgrade | Upgrade instance with the given list of addons


# **cancel_instance**
> CancelInstanceResponse cancel_instance(x_request_id, instance_id)

Cancel specific instance by id

Your are free to cancel a previously created instance at any time.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.cancel_instance_response import CancelInstanceResponse
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancel specific instance by id
        api_response = api_instance.cancel_instance(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->cancel_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancel specific instance by id
        api_response = api_instance.cancel_instance(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->cancel_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the instance |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CancelInstanceResponse**](CancelInstanceResponse.md)

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

# **create_instance**
> CreateInstanceResponse create_instance(x_request_id, create_instance_request)

Create a new instance

Create a new instance for your account with the provided parameters.       <table>         <tr><th>ProductId</th><th>Product</th><th>Disk Size</th></tr>         <tr><td>V1</td><td>VPS S SSD</td><td>200 GB SSD</td></tr>         <tr><td>V12</td><td>VPS S NVMe</td><td>50 GB NVMe</td></tr>         <tr><td>V2</td><td>VPS M SSD</td><td>400 GB SSD</td></tr>         <tr><td>V13</td><td>VPS M NVMe</td><td>100 GB NVMe</td></tr>         <tr><td>V3</td><td>VPS L SSD</td><td>800 GB SSD</td></tr>         <tr><td>V14</td><td>VPS L NVMe</td><td>200 GB NVMe</td></tr>         <tr><td>V4</td><td>VPS XL SSD</td><td>1600 GB SSD</td></tr>         <tr><td>V15</td><td>VPS XL NVMe</td><td>400 GB NVMe</td></tr>         <tr><td>V8</td><td>VDS S</td><td>180 GB NVMe</td></tr>         <tr><td>V9</td><td>VDS M</td><td>240 GB NVMe</td></tr>         <tr><td>V10</td><td>VDS L</td><td>360 GB NVMe</td></tr>         <tr><td>V11</td><td>VDS XL</td><td>480 GB NVMe</td></tr>         <tr><td>V16</td><td>VDS XXL</td><td>720 GB NVMe</td></tr>         </table>

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.create_instance_request import CreateInstanceRequest
from pfruck_contabo.model.create_instance_response import CreateInstanceResponse
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_instance_request = CreateInstanceRequest(
        image_id="3f184ab8-a600-4e7c-8c9b-3413e21a3752",
        product_id="V3",
        region="EU",
        ssh_keys=[
            [123, 125],
        ],
        root_password=1,
        user_data='''#cloud-config
user: admin
timezone: Europe/Berlin
chpasswd:
 expire: False''',
        license="PleskHost",
        period=6,
        display_name="VPS",
    ) # CreateInstanceRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new instance
        api_response = api_instance.create_instance(x_request_id, create_instance_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->create_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new instance
        api_response = api_instance.create_instance(x_request_id, create_instance_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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
> PatchInstanceResponse patch_instance(x_request_id, instance_id, patch_instance_request)

Update specific instance

Update specific instance by instanceId.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.patch_instance_response import PatchInstanceResponse
from pfruck_contabo.model.patch_instance_request import PatchInstanceRequest
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    patch_instance_request = PatchInstanceRequest(
        display_name="VPS",
    ) # PatchInstanceRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update specific instance
        api_response = api_instance.patch_instance(x_request_id, instance_id, patch_instance_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->patch_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update specific instance
        api_response = api_instance.patch_instance(x_request_id, instance_id, patch_instance_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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
> ReinstallInstanceResponse reinstall_instance(x_request_id, instance_id, reinstall_instance_request)

Reinstall specific instance

You can reinstall a specific instance with a new image and optionally add ssh keys, a root password or cloud-init.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.reinstall_instance_request import ReinstallInstanceRequest
from pfruck_contabo.model.reinstall_instance_response import ReinstallInstanceResponse
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    reinstall_instance_request = ReinstallInstanceRequest(
        image_id="3f184ab8-a600-4e7c-8c9b-3413e21a3752",
        ssh_keys=[
            [123, 125],
        ],
        root_password=1,
        user_data='''#cloud-config
user: admin
timezone: Europe/Berlin
chpasswd:
 expire: False''',
    ) # ReinstallInstanceRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reinstall specific instance
        api_response = api_instance.reinstall_instance(x_request_id, instance_id, reinstall_instance_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->reinstall_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reinstall specific instance
        api_response = api_instance.reinstall_instance(x_request_id, instance_id, reinstall_instance_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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

# **retrieve_instance**
> FindInstanceResponse retrieve_instance(x_request_id, instance_id)

Get specific instance by id

Get attributes values to a specific instance on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.find_instance_response import FindInstanceResponse
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific instance by id
        api_response = api_instance.retrieve_instance(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->retrieve_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific instance by id
        api_response = api_instance.retrieve_instance(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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
> ListInstancesResponse retrieve_instances_list(x_request_id)

List instances

List and filter all instances in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.list_instances_response import ListInstancesResponse
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = "vmd12345" # str | The name of the instance (optional)
    region = "EU" # str | The Region of the instance (optional)
    instance_id = 100 # int | The identifier of the instance (deprecated) (optional)
    instance_ids = "100, 101, 102" # str | Comma separated instances identifiers (optional)
    status = "provisioning,installing" # str | The status of the instance (optional)
    add_on_ids = "1044,827" # str | Identifiers of Addons the instances have (optional)

    # example passing only required values which don't have defaults set
    try:
        # List instances
        api_response = api_instance.retrieve_instances_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->retrieve_instances_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List instances
        api_response = api_instance.retrieve_instances_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, region=region, instance_id=instance_id, instance_ids=instance_ids, status=status, add_on_ids=add_on_ids)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->retrieve_instances_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **name** | **str**| The name of the instance | [optional]
 **region** | **str**| The Region of the instance | [optional]
 **instance_id** | **int**| The identifier of the instance (deprecated) | [optional]
 **instance_ids** | **str**| Comma separated instances identifiers | [optional]
 **status** | **str**| The status of the instance | [optional]
 **add_on_ids** | **str**| Identifiers of Addons the instances have | [optional]

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
> UpgradeInstanceResponse upgrade_instance(x_request_id, instance_id, upgrade_instance_request)

Upgrade instance with the given list of addons

You can upgrade instance with the given list of addons.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instances_api
from pfruck_contabo.model.upgrade_instance_response import UpgradeInstanceResponse
from pfruck_contabo.model.upgrade_instance_request import UpgradeInstanceRequest
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
    api_instance = instances_api.InstancesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    upgrade_instance_request = UpgradeInstanceRequest(
        add_ons=[
            [123, 125],
        ],
    ) # UpgradeInstanceRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upgrade instance with the given list of addons
        api_response = api_instance.upgrade_instance(x_request_id, instance_id, upgrade_instance_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstancesApi->upgrade_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upgrade instance with the given list of addons
        api_response = api_instance.upgrade_instance(x_request_id, instance_id, upgrade_instance_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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

[**UpgradeInstanceResponse**](UpgradeInstanceResponse.md)

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

