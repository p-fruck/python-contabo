# pfruck_contabo.InstanceActionsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restart**](InstanceActionsApi.md#restart) | **POST** /v1/compute/instances/{instanceId}/actions/restart | Restart a compute instance / resource identified by its id
[**shutdown**](InstanceActionsApi.md#shutdown) | **POST** /v1/compute/instances/{instanceId}/actions/shutdown | Shutdown compute instance / resource by its id
[**start**](InstanceActionsApi.md#start) | **POST** /v1/compute/instances/{instanceId}/actions/start | Start a compute instance / resource identified by its id
[**stop**](InstanceActionsApi.md#stop) | **POST** /v1/compute/instances/{instanceId}/actions/stop | Stop compute instance / resource by its id


# **restart**
> InstanceRestartActionResponse restart(x_request_id, instance_id)

Restart a compute instance / resource identified by its id

Restarting a compute instance / resource is like powering off and powering on again a real server. If the compute instance / resource is already started it will stopped and started again. If it is stopped the compute instance / resource will be started. So please be aware that data may be lost. You may check the current status anytime when getting information about a compute instance / resource.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instance_actions_api
from pfruck_contabo.model.instance_restart_action_response import InstanceRestartActionResponse
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
    api_instance = instance_actions_api.InstanceActionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restart a compute instance / resource identified by its id
        api_response = api_instance.restart(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->restart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restart a compute instance / resource identified by its id
        api_response = api_instance.restart(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->restart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the compute instance / resource to be started. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**InstanceRestartActionResponse**](InstanceRestartActionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information of restarted instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown**
> InstanceShutdownActionResponse shutdown(x_request_id, instance_id)

Shutdown compute instance / resource by its id

Shutdown an compute instance / resource. This is similar to pressing the power button on a physical machine. This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instance_actions_api
from pfruck_contabo.model.instance_shutdown_action_response import InstanceShutdownActionResponse
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
    api_instance = instance_actions_api.InstanceActionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance to be shutdown
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Shutdown compute instance / resource by its id
        api_response = api_instance.shutdown(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->shutdown: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Shutdown compute instance / resource by its id
        api_response = api_instance.shutdown(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->shutdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the instance to be shutdown |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**InstanceShutdownActionResponse**](InstanceShutdownActionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information of a shutdown instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> InstanceStartActionResponse start(x_request_id, instance_id)

Start a compute instance / resource identified by its id

Starting a compute instance / resource is like powering on a real server. If the compute instance / resource is already started nothing will happen. You may check the current status anytime when getting information about a compute instance / resource.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instance_actions_api
from pfruck_contabo.model.instance_start_action_response import InstanceStartActionResponse
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
    api_instance = instance_actions_api.InstanceActionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start a compute instance / resource identified by its id
        api_response = api_instance.start(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a compute instance / resource identified by its id
        api_response = api_instance.start(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the compute instance / resource to be started. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**InstanceStartActionResponse**](InstanceStartActionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information of started instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> InstanceStopActionResponse stop(x_request_id, instance_id)

Stop compute instance / resource by its id

Stopping a compute instance / resource is like powering off a real server. So please be aware that data may be lost. Alternatively you may log in and shut your compute instance / resource gracefully via the operating system. If the compute instance / resource is already stopped nothing will happen. You may check the current status anytime when getting information about a compute instance / resource.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instance_actions_api
from pfruck_contabo.model.instance_stop_action_response import InstanceStopActionResponse
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
    api_instance = instance_actions_api.InstanceActionsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance to stop
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop compute instance / resource by its id
        api_response = api_instance.stop(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop compute instance / resource by its id
        api_response = api_instance.stop(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the instance to stop |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**InstanceStopActionResponse**](InstanceStopActionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information of stoped instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

