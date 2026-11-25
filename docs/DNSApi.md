# pfruck_contabo.DNSApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_dns_zone_records**](DNSApi.md#bulk_delete_dns_zone_records) | **DELETE** /v1/dns/zones/{zoneName}/records/bulk | Bulk delete DNS zone records
[**create_dns_zone**](DNSApi.md#create_dns_zone) | **POST** /v1/dns/zones | Create DNS zone
[**create_dns_zone_record**](DNSApi.md#create_dns_zone_record) | **POST** /v1/dns/zones/{zoneName}/records | Create DNS zone record
[**create_ptr_record**](DNSApi.md#create_ptr_record) | **POST** /v1/dns/ptrs | Create a new PTR Record using ip address
[**delete_dns_zone**](DNSApi.md#delete_dns_zone) | **DELETE** /v1/dns/zones/{zoneName} | Delete a DNS zone.
[**delete_dns_zone_record**](DNSApi.md#delete_dns_zone_record) | **DELETE** /v1/dns/zones/{zoneName}/records/{recordId} | Delete a DNS zone record
[**delete_ptr_record**](DNSApi.md#delete_ptr_record) | **DELETE** /v1/dns/ptrs/{ipAddress} | Delete a PTR Record using ip address
[**retrieve_dns_zone**](DNSApi.md#retrieve_dns_zone) | **GET** /v1/dns/zones/{zoneName} | Retrieve a DNS Zone by zone name
[**retrieve_dns_zone_records_list**](DNSApi.md#retrieve_dns_zone_records_list) | **GET** /v1/dns/zones/{zoneName}/records | List a DNS Zone&#39;s records
[**retrieve_dns_zones_list**](DNSApi.md#retrieve_dns_zones_list) | **GET** /v1/dns/zones | List DNS zones
[**retrieve_ptr_record**](DNSApi.md#retrieve_ptr_record) | **GET** /v1/dns/ptrs/{ipAddress} | Retrieve a PTR Record by ip address
[**retrieve_ptr_records_list**](DNSApi.md#retrieve_ptr_records_list) | **GET** /v1/dns/ptrs | List PTR records
[**update_dns_zone_record**](DNSApi.md#update_dns_zone_record) | **PATCH** /v1/dns/zones/{zoneName}/records/{recordId} | Update DNS zone record
[**update_ptr_record**](DNSApi.md#update_ptr_record) | **PUT** /v1/dns/ptrs/{ipAddress} | Edit a PTR Record by ip address


# **bulk_delete_dns_zone_records**
> ApiBulkDeleteDnsZoneRecordsResponse bulk_delete_dns_zone_records(x_request_id, zone_name, bulk_delete_dns_zone_records_request, x_trace_id=x_trace_id)

Bulk delete DNS zone records

Delete multiple zone records from a DNS Zone

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.api_bulk_delete_dns_zone_records_response import ApiBulkDeleteDnsZoneRecordsResponse
from pfruck_contabo.models.bulk_delete_dns_zone_records_request import BulkDeleteDnsZoneRecordsRequest
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    zone_name = 'example.com' # str | Zone name
    bulk_delete_dns_zone_records_request = pfruck_contabo.BulkDeleteDnsZoneRecordsRequest() # BulkDeleteDnsZoneRecordsRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Bulk delete DNS zone records
        api_response = api_instance.bulk_delete_dns_zone_records(x_request_id, zone_name, bulk_delete_dns_zone_records_request, x_trace_id=x_trace_id)
        print("The response of DNSApi->bulk_delete_dns_zone_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->bulk_delete_dns_zone_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **zone_name** | **str**| Zone name | 
 **bulk_delete_dns_zone_records_request** | [**BulkDeleteDnsZoneRecordsRequest**](BulkDeleteDnsZoneRecordsRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ApiBulkDeleteDnsZoneRecordsResponse**](ApiBulkDeleteDnsZoneRecordsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed result for bulk deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dns_zone**
> ApiDnsZoneResponse create_dns_zone(x_request_id, create_dns_zone_request, x_trace_id=x_trace_id)

Create DNS zone

Creates a new DNS zone for a customer

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.api_dns_zone_response import ApiDnsZoneResponse
from pfruck_contabo.models.create_dns_zone_request import CreateDnsZoneRequest
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_dns_zone_request = pfruck_contabo.CreateDnsZoneRequest() # CreateDnsZoneRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create DNS zone
        api_response = api_instance.create_dns_zone(x_request_id, create_dns_zone_request, x_trace_id=x_trace_id)
        print("The response of DNSApi->create_dns_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->create_dns_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **create_dns_zone_request** | [**CreateDnsZoneRequest**](CreateDnsZoneRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ApiDnsZoneResponse**](ApiDnsZoneResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard DNS Zone attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dns_zone_record**
> ApiDnsZoneRecordResponse create_dns_zone_record(x_request_id, zone_name, create_dns_zone_record_request, x_trace_id=x_trace_id)

Create DNS zone record

Create resource record in a zone

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.api_dns_zone_record_response import ApiDnsZoneRecordResponse
from pfruck_contabo.models.create_dns_zone_record_request import CreateDnsZoneRecordRequest
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    zone_name = 'example.com' # str | Zone name
    create_dns_zone_record_request = pfruck_contabo.CreateDnsZoneRecordRequest() # CreateDnsZoneRecordRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create DNS zone record
        api_response = api_instance.create_dns_zone_record(x_request_id, zone_name, create_dns_zone_record_request, x_trace_id=x_trace_id)
        print("The response of DNSApi->create_dns_zone_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->create_dns_zone_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **zone_name** | **str**| Zone name | 
 **create_dns_zone_record_request** | [**CreateDnsZoneRecordRequest**](CreateDnsZoneRecordRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ApiDnsZoneRecordResponse**](ApiDnsZoneRecordResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard record attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ptr_record**
> ApiPtrRecordResponse create_ptr_record(x_request_id, create_ptr_record_request, x_trace_id=x_trace_id)

Create a new PTR Record using ip address

Create a new PTR Record using ip address. Only IPv6 can be created

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.api_ptr_record_response import ApiPtrRecordResponse
from pfruck_contabo.models.create_ptr_record_request import CreatePtrRecordRequest
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_ptr_record_request = pfruck_contabo.CreatePtrRecordRequest() # CreatePtrRecordRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create a new PTR Record using ip address
        api_response = api_instance.create_ptr_record(x_request_id, create_ptr_record_request, x_trace_id=x_trace_id)
        print("The response of DNSApi->create_ptr_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->create_ptr_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **create_ptr_record_request** | [**CreatePtrRecordRequest**](CreatePtrRecordRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ApiPtrRecordResponse**](ApiPtrRecordResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard PTR Record attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_zone**
> delete_dns_zone(x_request_id, zone_name, x_trace_id=x_trace_id)

Delete a DNS zone.

Delete a DNS Zone using zone name.

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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    zone_name = 'example.com' # str | Zone name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Delete a DNS zone.
        api_instance.delete_dns_zone(x_request_id, zone_name, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DNSApi->delete_dns_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **zone_name** | **str**| Zone name | 
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

# **delete_dns_zone_record**
> delete_dns_zone_record(x_request_id, record_id, zone_name, x_trace_id=x_trace_id)

Delete a DNS zone record

Delete a DNZ Zone's record

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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    record_id = 12345 # int | The identifier of the DNS record
    zone_name = 'example.com' # str | Zone name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Delete a DNS zone record
        api_instance.delete_dns_zone_record(x_request_id, record_id, zone_name, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DNSApi->delete_dns_zone_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **record_id** | **int**| The identifier of the DNS record | 
 **zone_name** | **str**| Zone name | 
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

# **delete_ptr_record**
> delete_ptr_record(x_request_id, ip_address, x_trace_id=x_trace_id)

Delete a PTR Record using ip address

Delete a PTR Record using ip address. Only IPv6 can be deleted

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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    ip_address = '11.10.2.3' # str | Ip Address
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Delete a PTR Record using ip address
        api_instance.delete_ptr_record(x_request_id, ip_address, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DNSApi->delete_ptr_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **ip_address** | **str**| Ip Address | 
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

# **retrieve_dns_zone**
> retrieve_dns_zone(x_request_id, zone_name, x_trace_id=x_trace_id)

Retrieve a DNS Zone by zone name

Get all attributes for a specific DNS Zone

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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    zone_name = 'example.com' # str | Zone name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Retrieve a DNS Zone by zone name
        api_instance.retrieve_dns_zone(x_request_id, zone_name, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DNSApi->retrieve_dns_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **zone_name** | **str**| Zone name | 
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
**200** | The response will be a JSON object and contains standard DNS Zone attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dns_zone_records_list**
> ListDnsZoneRecordsResponse retrieve_dns_zone_records_list(x_request_id, zone_name, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, search=search)

List a DNS Zone's records

Get all the records of a DNS Zone

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_dns_zone_records_response import ListDnsZoneRecordsResponse
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    zone_name = 'example.com' # str | Zone name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    search = 'example.com' # str | Search DNS records by name, type or data (optional)

    try:
        # List a DNS Zone's records
        api_response = api_instance.retrieve_dns_zone_records_list(x_request_id, zone_name, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, search=search)
        print("The response of DNSApi->retrieve_dns_zone_records_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->retrieve_dns_zone_records_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **zone_name** | **str**| Zone name | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **search** | **str**| Search DNS records by name, type or data | [optional] 

### Return type

[**ListDnsZoneRecordsResponse**](ListDnsZoneRecordsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a paginated list of dns zone records. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dns_zones_list**
> ListDnsZonesResponse retrieve_dns_zones_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, customer_id=customer_id, tenant_id=tenant_id, zone_name=zone_name)

List DNS zones

Get a list of all zones

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_dns_zones_response import ListDnsZonesResponse
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    customer_id = '54321' # str | Customer ID (optional)
    tenant_id = 'DE' # str | Tenant ID (optional)
    zone_name = 'example.com' # str | Seach by zone name (optional)

    try:
        # List DNS zones
        api_response = api_instance.retrieve_dns_zones_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, customer_id=customer_id, tenant_id=tenant_id, zone_name=zone_name)
        print("The response of DNSApi->retrieve_dns_zones_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->retrieve_dns_zones_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **customer_id** | **str**| Customer ID | [optional] 
 **tenant_id** | **str**| Tenant ID | [optional] 
 **zone_name** | **str**| Seach by zone name | [optional] 

### Return type

[**ListDnsZonesResponse**](ListDnsZonesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a json object which will contain a paginated list of dns zones. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_ptr_record**
> ApiPtrRecordResponse retrieve_ptr_record(x_request_id, ip_address, x_trace_id=x_trace_id)

Retrieve a PTR Record by ip address

Get all attributes for a specific PTR Record

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.api_ptr_record_response import ApiPtrRecordResponse
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    ip_address = '11.10.2.3' # str | Ip Address
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Retrieve a PTR Record by ip address
        api_response = api_instance.retrieve_ptr_record(x_request_id, ip_address, x_trace_id=x_trace_id)
        print("The response of DNSApi->retrieve_ptr_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->retrieve_ptr_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **ip_address** | **str**| Ip Address | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ApiPtrRecordResponse**](ApiPtrRecordResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard PTR Record attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_ptr_records_list**
> ListPtrRecordsResponse retrieve_ptr_records_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, customer_id=customer_id, tenant_id=tenant_id, ips=ips, search=search)

List PTR records

Get a list of all PTR records, either customer or a list of IPs is required

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_ptr_records_response import ListPtrRecordsResponse
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    customer_id = '54321' # str | Customer ID (optional)
    tenant_id = 'DE' # str | Tenant ID (optional)
    ips = ['ips_example'] # List[str] | List of IPs, separated by commas (optional)
    search = 'vmd1111.contabo.net' # str | Search PTR records by ip or data (optional)

    try:
        # List PTR records
        api_response = api_instance.retrieve_ptr_records_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, customer_id=customer_id, tenant_id=tenant_id, ips=ips, search=search)
        print("The response of DNSApi->retrieve_ptr_records_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->retrieve_ptr_records_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **customer_id** | **str**| Customer ID | [optional] 
 **tenant_id** | **str**| Tenant ID | [optional] 
 **ips** | [**List[str]**](str.md)| List of IPs, separated by commas | [optional] 
 **search** | **str**| Search PTR records by ip or data | [optional] 

### Return type

[**ListPtrRecordsResponse**](ListPtrRecordsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a paginated list of ptr records. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_zone_record**
> ApiDnsZoneRecordResponse update_dns_zone_record(x_request_id, record_id, zone_name, update_dns_zone_record_request, x_trace_id=x_trace_id)

Update DNS zone record

Create resource record in a zone

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.api_dns_zone_record_response import ApiDnsZoneRecordResponse
from pfruck_contabo.models.update_dns_zone_record_request import UpdateDnsZoneRecordRequest
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    record_id = 12345 # int | The identifier of the DNS record
    zone_name = 'example.com' # str | Zone name
    update_dns_zone_record_request = pfruck_contabo.UpdateDnsZoneRecordRequest() # UpdateDnsZoneRecordRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update DNS zone record
        api_response = api_instance.update_dns_zone_record(x_request_id, record_id, zone_name, update_dns_zone_record_request, x_trace_id=x_trace_id)
        print("The response of DNSApi->update_dns_zone_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->update_dns_zone_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **record_id** | **int**| The identifier of the DNS record | 
 **zone_name** | **str**| Zone name | 
 **update_dns_zone_record_request** | [**UpdateDnsZoneRecordRequest**](UpdateDnsZoneRecordRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ApiDnsZoneRecordResponse**](ApiDnsZoneRecordResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard record attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ptr_record**
> update_ptr_record(x_request_id, ip_address, update_ptr_record_request, x_trace_id=x_trace_id)

Edit a PTR Record by ip address

Edit attributes for a specific PTR Record

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.update_ptr_record_request import UpdatePtrRecordRequest
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
    api_instance = pfruck_contabo.DNSApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    ip_address = '11.10.2.3' # str | Ip Address
    update_ptr_record_request = pfruck_contabo.UpdatePtrRecordRequest() # UpdatePtrRecordRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Edit a PTR Record by ip address
        api_instance.update_ptr_record(x_request_id, ip_address, update_ptr_record_request, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DNSApi->update_ptr_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **ip_address** | **str**| Ip Address | 
 **update_ptr_record_request** | [**UpdatePtrRecordRequest**](UpdatePtrRecordRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body has no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

