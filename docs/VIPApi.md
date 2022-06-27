# pfruck_contabo.VIPApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_vip**](VIPApi.md#retrieve_vip) | **GET** /v1/vips/{vipId} | Get specific VIP by id
[**retrieve_vip_list**](VIPApi.md#retrieve_vip_list) | **GET** /v1/vips | List VIPs


# **retrieve_vip**
> FindVipResponse retrieve_vip(x_request_id, vip_id)

Get specific VIP by id

Get attributes values to a specific VIP on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import vip_api
from pfruck_contabo.model.find_vip_response import FindVipResponse
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
    api_instance = vip_api.VIPApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    vip_id = "a846c6cc-731c-45dc-b653-bc8232e88d9c" # str | The identifier of the VIP
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific VIP by id
        api_response = api_instance.retrieve_vip(x_request_id, vip_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling VIPApi->retrieve_vip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific VIP by id
        api_response = api_instance.retrieve_vip(x_request_id, vip_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling VIPApi->retrieve_vip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **vip_id** | **str**| The identifier of the VIP |
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
> ListVipResponse retrieve_vip_list(x_request_id)

List VIPs

List and filter all vips in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import vip_api
from pfruck_contabo.model.list_vip_response import ListVipResponse
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
    api_instance = vip_api.VIPApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    resource_id = "10001" # str | The resourceId using the VIP. (optional)
    resource_type = "instance" # str | The resourceType using the VIP. (optional)
    resource_name = "vmi100101" # str | The name of the resource. (optional)
    resource_display_name = "my instance" # str | The display name of the resource. (optional)
    ip_version = "v4" # str | The VIP version. (optional)
    ip = "192.168.1.1" # str | The ip of the VIP. (optional)
    type = "fixed" # str | The VIP type. (optional)
    data_center = "European Union (Germany) 3" # str | The dataCenter of the VIP. (optional)
    region = "European Union (Germany)" # str | The region of the VIP. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List VIPs
        api_response = api_instance.retrieve_vip_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling VIPApi->retrieve_vip_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List VIPs
        api_response = api_instance.retrieve_vip_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, resource_id=resource_id, resource_type=resource_type, resource_name=resource_name, resource_display_name=resource_display_name, ip_version=ip_version, ip=ip, type=type, data_center=data_center, region=region)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling VIPApi->retrieve_vip_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **resource_id** | **str**| The resourceId using the VIP. | [optional]
 **resource_type** | **str**| The resourceType using the VIP. | [optional]
 **resource_name** | **str**| The name of the resource. | [optional]
 **resource_display_name** | **str**| The display name of the resource. | [optional]
 **ip_version** | **str**| The VIP version. | [optional]
 **ip** | **str**| The ip of the VIP. | [optional]
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

