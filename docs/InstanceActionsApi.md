# pfruck_contabo.InstanceActionsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rescue**](InstanceActionsApi.md#rescue) | **POST** /v1/compute/instances/{instanceId}/actions/rescue | Rescue a compute instance / resource identified by its id
[**reset_password_action**](InstanceActionsApi.md#reset_password_action) | **POST** /v1/compute/instances/{instanceId}/actions/resetPassword | Reset password for a compute instance / resource referenced by an id
[**restart**](InstanceActionsApi.md#restart) | **POST** /v1/compute/instances/{instanceId}/actions/restart | Restart a compute instance / resource identified by its id.
[**shutdown**](InstanceActionsApi.md#shutdown) | **POST** /v1/compute/instances/{instanceId}/actions/shutdown | Shutdown compute instance / resource by its id
[**start**](InstanceActionsApi.md#start) | **POST** /v1/compute/instances/{instanceId}/actions/start | Start a compute instance / resource identified by its id
[**stop**](InstanceActionsApi.md#stop) | **POST** /v1/compute/instances/{instanceId}/actions/stop | Stop compute instance / resource by its id


# **rescue**
> InstanceRescueActionResponse rescue(x_request_id, instance_id, instances_actions_rescue_request)

Rescue a compute instance / resource identified by its id

You can reboot your instance in rescue mode to resolve system issues. Rescue system is Linux based and its booted instead of your regular operating system. The disk containing your operating sytstem, software and your data is already mounted for you to access and repair/modify files. After a reboot your compute instance will boot your operating system. Please note that this is for advanced users.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instance_actions_api
from pfruck_contabo.model.instances_actions_rescue_request import InstancesActionsRescueRequest
from pfruck_contabo.model.instance_rescue_action_response import InstanceRescueActionResponse
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
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started in rescue mode.
    instances_actions_rescue_request = InstancesActionsRescueRequest(
        root_password=1,
        ssh_keys=[
            [123, 125],
        ],
        user_data='''#cloud-config
user: root
ssh_pwauth: true
disable_root: false
ssh_authorized_keys:
  - <sshkey>
chpasswd:
  list:
    - root:<password> 
 expire: False
''',
    ) # InstancesActionsRescueRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Rescue a compute instance / resource identified by its id
        api_response = api_instance.rescue(x_request_id, instance_id, instances_actions_rescue_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->rescue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rescue a compute instance / resource identified by its id
        api_response = api_instance.rescue(x_request_id, instance_id, instances_actions_rescue_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->rescue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the compute instance / resource to be started in rescue mode. |
 **instances_actions_rescue_request** | [**InstancesActionsRescueRequest**](InstancesActionsRescueRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**InstanceRescueActionResponse**](InstanceRescueActionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information of rescued instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_action**
> InstanceResetPasswordActionResponse reset_password_action(x_request_id, instance_id, instances_reset_password_actions_request)

Reset password for a compute instance / resource referenced by an id

Reset password for a compute instance / resource referenced by an id. This will reset the current password to the password that you provided in the body of this request.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import instance_actions_api
from pfruck_contabo.model.instances_reset_password_actions_request import InstancesResetPasswordActionsRequest
from pfruck_contabo.model.instance_reset_password_action_response import InstanceResetPasswordActionResponse
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
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started in rescue mode.
    instances_reset_password_actions_request = InstancesResetPasswordActionsRequest(
        ssh_keys=[
            [123, 125],
        ],
        root_password=1,
        user_data='''#cloud-config
user: root
ssh_pwauth: true
disable_root: false
ssh_authorized_keys:
  - <sshkey>
chpasswd:
  list:
    - root:<password> 
 expire: False
''',
    ) # InstancesResetPasswordActionsRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset password for a compute instance / resource referenced by an id
        api_response = api_instance.reset_password_action(x_request_id, instance_id, instances_reset_password_actions_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->reset_password_action: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset password for a compute instance / resource referenced by an id
        api_response = api_instance.reset_password_action(x_request_id, instance_id, instances_reset_password_actions_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->reset_password_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the compute instance / resource to be started in rescue mode. |
 **instances_reset_password_actions_request** | [**InstancesResetPasswordActionsRequest**](InstancesResetPasswordActionsRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**InstanceResetPasswordActionResponse**](InstanceResetPasswordActionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Information of an instance password reset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart**
> InstanceRestartActionResponse restart(x_request_id, instance_id)

Restart a compute instance / resource identified by its id.

To restart a compute instance that has been identified by its id, you should perform a restart action on it.

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
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started in rescue mode.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restart a compute instance / resource identified by its id.
        api_response = api_instance.restart(x_request_id, instance_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->restart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restart a compute instance / resource identified by its id.
        api_response = api_instance.restart(x_request_id, instance_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling InstanceActionsApi->restart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **instance_id** | **int**| The identifier of the compute instance / resource to be started in rescue mode. |
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
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started in rescue mode.
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
 **instance_id** | **int**| The identifier of the compute instance / resource to be started in rescue mode. |
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
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started in rescue mode.
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
 **instance_id** | **int**| The identifier of the compute instance / resource to be started in rescue mode. |
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
    instance_id = 12345 # int | The identifier of the compute instance / resource to be started in rescue mode.
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
 **instance_id** | **int**| The identifier of the compute instance / resource to be started in rescue mode. |
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

