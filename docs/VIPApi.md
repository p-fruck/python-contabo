# pfruck_contabo.VIPApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_ip**](VIPApi.md#assign_ip) | **POST** /v1/vips/{ip}/{resourceType}/{resourceId} | Assign a VIP to an VPS/VDS/Bare Metal
[**retrieve_vip**](VIPApi.md#retrieve_vip) | **GET** /v1/vips/{ip} | Get specific VIP by ip
[**retrieve_vip_list**](VIPApi.md#retrieve_vip_list) | **GET** /v1/vips | List VIPs
[**unassign_ip**](VIPApi.md#unassign_ip) | **DELETE** /v1/vips/{ip}/{resourceType}/{resourceId} | Unassign a VIP to a VPS/VDS/Bare Metal


# **assign_ip**
> AssignVipResponse assign_ip(x_request_id, resource_id, ip, resource_type, x_trace_id=x_trace_id)

Assign a VIP to an VPS/VDS/Bare Metal

Assign a VIP to a VPS/VDS/Bare Metal using the machine id.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.assign_vip_response import AssignVipResponse
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
    api_instance = pfruck_contabo.VIPApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    resource_id = 12345 # int | The identifier of the resource
    ip = '127.0.0.1' # str | The ip you want to add the instance to
    resource_type = 'instances' # str | The resourceType using the VIP.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Assign a VIP to an VPS/VDS/Bare Metal
        api_response = api_instance.assign_ip(x_request_id, resource_id, ip, resource_type, x_trace_id=x_trace_id)
        print("The response of VIPApi->assign_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VIPApi->assign_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **resource_id** | **int**| The identifier of the resource | 
 **ip** | **str**| The ip you want to add the instance to | 
 **resource_type** | **str**| The resourceType using the VIP. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**AssignVipResponse**](AssignVipResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard VIP attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vip**
> FindVipResponse retrieve_vip(x_request_id, ip, x_trace_id=x_trace_id)

Get specific VIP by ip

Get attributes values to a specific VIP on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_vip_response import FindVipResponse
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
    api_instance = pfruck_contabo.VIPApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    ip = '10.214.121.145' # str | The ip of the VIP
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get specific VIP by ip
        api_response = api_instance.retrieve_vip(x_request_id, ip, x_trace_id=x_trace_id)
        print("The response of VIPApi->retrieve_vip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VIPApi->retrieve_vip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **ip** | **str**| The ip of the VIP | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindVipResponse**](FindVipResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard VIP attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vip_list**
> ListVipResponse retrieve_vip_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, resource_id=resource_id, resource_type=resource_type, resource_name=resource_name, resource_display_name=resource_display_name, ip_version=ip_version, ips=ips, ip=ip, type=type, data_center=data_center, region=region)

List VIPs

List and filter all vips in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_vip_response import ListVipResponse
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
    api_instance = pfruck_contabo.VIPApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    resource_id = '10001' # str | The resourceId using the VIP. (optional)
    resource_type = 'instances' # str | The resourceType using the VIP. (optional)
    resource_name = 'vmi100101' # str | The name of the resource. (optional)
    resource_display_name = 'my instance' # str | The display name of the resource. (optional)
    ip_version = 'v4' # str | The VIP version. (optional)
    ips = '10.214.121.145, 10.214.121.1, 10.214.121.11' # str | Comma separated IPs (optional)
    ip = '10.214.121.145' # str | The ip of the VIP (optional)
    type = 'additional' # str | The VIP type. (optional)
    data_center = 'European Union (Germany) 3' # str | The dataCenter of the VIP. (optional)
    region = 'EU' # str | The region of the VIP. (optional)

    try:
        # List VIPs
        api_response = api_instance.retrieve_vip_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, resource_id=resource_id, resource_type=resource_type, resource_name=resource_name, resource_display_name=resource_display_name, ip_version=ip_version, ips=ips, ip=ip, type=type, data_center=data_center, region=region)
        print("The response of VIPApi->retrieve_vip_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VIPApi->retrieve_vip_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **resource_id** | **str**| The resourceId using the VIP. | [optional] 
 **resource_type** | **str**| The resourceType using the VIP. | [optional] 
 **resource_name** | **str**| The name of the resource. | [optional] 
 **resource_display_name** | **str**| The display name of the resource. | [optional] 
 **ip_version** | **str**| The VIP version. | [optional] 
 **ips** | **str**| Comma separated IPs | [optional] 
 **ip** | **str**| The ip of the VIP | [optional] 
 **type** | **str**| The VIP type. | [optional] 
 **data_center** | **str**| The dataCenter of the VIP. | [optional] 
 **region** | **str**| The region of the VIP. | [optional] 

### Return type

[**ListVipResponse**](ListVipResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of Vips. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_ip**
> unassign_ip(x_request_id, resource_id, ip, resource_type, x_trace_id=x_trace_id)

Unassign a VIP to a VPS/VDS/Bare Metal

Unassign a VIP from an VPS/VDS/Bare Metal using the machine id.

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
    api_instance = pfruck_contabo.VIPApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    resource_id = 12345 # int | The identifier of the resource
    ip = '127.0.0.1' # str | The ip you want to add the instance to
    resource_type = 'instances' # str | The resourceType using the VIP.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Unassign a VIP to a VPS/VDS/Bare Metal
        api_instance.unassign_ip(x_request_id, resource_id, ip, resource_type, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling VIPApi->unassign_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **resource_id** | **int**| The identifier of the resource | 
 **ip** | **str**| The ip you want to add the instance to | 
 **resource_type** | **str**| The resourceType using the VIP. | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

