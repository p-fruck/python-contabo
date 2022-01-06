# pfruck_contabo.InstancesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_instance**](InstancesApi.md#cancel_instance) | **POST** /v1/compute/instances/{instanceId}/cancel | Cancel specific instance by id
[**create_instance**](InstancesApi.md#create_instance) | **POST** /v1/compute/instances | Create a new instance
[**reinstall_instance**](InstancesApi.md#reinstall_instance) | **PATCH** /v1/compute/instances/{instanceId} | Reinstall specific instance
[**retrieve_instance**](InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
[**retrieve_instances_list**](InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances

# **cancel_instance**
> CancelInstanceResponse cancel_instance(x_request_id, instance_id, x_trace_id=x_trace_id)

Cancel specific instance by id

Your are free to cancel a previously created instance at any time.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InstancesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Cancel specific instance by id
    api_response = api_instance.cancel_instance(x_request_id, instance_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_instance**
> CreateInstanceResponse create_instance(body, x_request_id, x_trace_id=x_trace_id)

Create a new instance

Create a new instance for your account with the provided parameters.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InstancesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateInstanceRequest() # CreateInstanceRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new instance
    api_response = api_instance.create_instance(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->create_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInstanceRequest**](CreateInstanceRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateInstanceResponse**](CreateInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reinstall_instance**
> ReinstallInstanceResponse reinstall_instance(body, x_request_id, instance_id, x_trace_id=x_trace_id)

Reinstall specific instance

You can reinstall a specific instance with a new image and optionally add ssh keys, a root password or cloud-init.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InstancesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.ReinstallInstanceRequest() # ReinstallInstanceRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Reinstall specific instance
    api_response = api_instance.reinstall_instance(body, x_request_id, instance_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->reinstall_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReinstallInstanceRequest**](ReinstallInstanceRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ReinstallInstanceResponse**](ReinstallInstanceResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_instance**
> FindInstanceResponse retrieve_instance(x_request_id, instance_id, x_trace_id=x_trace_id)

Get specific instance by id

Get attributes values to a specific instance on your account.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InstancesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get specific instance by id
    api_response = api_instance.retrieve_instance(x_request_id, instance_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_instances_list**
> ListInstancesResponse retrieve_instances_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, region=region, instance_id=instance_id, status=status)

List instances

List and filter all instances in your account

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InstancesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
name = 'name_example' # str | The name of the instance (optional)
region = 'region_example' # str | The Region of the instance (optional)
instance_id = 789 # int | The identifier of the instance (optional)
status = 'status_example' # str | The status of the instance (optional)

try:
    # List instances
    api_response = api_instance.retrieve_instances_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, region=region, instance_id=instance_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->retrieve_instances_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of the instance | [optional] 
 **region** | **str**| The Region of the instance | [optional] 
 **instance_id** | **int**| The identifier of the instance | [optional] 
 **status** | **str**| The status of the instance | [optional] 

### Return type

[**ListInstancesResponse**](ListInstancesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

