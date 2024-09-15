# pfruck_contabo.ObjectStoragesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_object_storage**](ObjectStoragesApi.md#cancel_object_storage) | **PATCH** /v1/object-storages/{objectStorageId}/cancel | Cancels the specified object storage at the next possible date
[**create_object_storage**](ObjectStoragesApi.md#create_object_storage) | **POST** /v1/object-storages | Create a new object storage
[**retrieve_data_center_list**](ObjectStoragesApi.md#retrieve_data_center_list) | **GET** /v1/data-centers | List data centers
[**retrieve_object_storage**](ObjectStoragesApi.md#retrieve_object_storage) | **GET** /v1/object-storages/{objectStorageId} | Get specific object storage by its id
[**retrieve_object_storage_list**](ObjectStoragesApi.md#retrieve_object_storage_list) | **GET** /v1/object-storages | List all your object storages
[**retrieve_object_storages_stats**](ObjectStoragesApi.md#retrieve_object_storages_stats) | **GET** /v1/object-storages/{objectStorageId}/stats | List usage statistics about the specified object storage
[**update_object_storage**](ObjectStoragesApi.md#update_object_storage) | **PATCH** /v1/object-storages/{objectStorageId} | Modifies the display name of object storage
[**upgrade_object_storage**](ObjectStoragesApi.md#upgrade_object_storage) | **POST** /v1/object-storages/{objectStorageId}/resize | Upgrade object storage size resp. update autoscaling settings.


# **cancel_object_storage**
> CancelObjectStorageResponse cancel_object_storage(x_request_id, object_storage_id, body, x_trace_id=x_trace_id)

Cancels the specified object storage at the next possible date

Cancels the specified object storage at the next possible date. Please be aware of your contract periods.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_object_storage_response import CancelObjectStorageResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = '4a6f95be-2ac0-4e3c-8eed-0dc67afed640' # str | The identifier of the object storage.
    body = None # object | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Cancels the specified object storage at the next possible date
        api_response = api_instance.cancel_object_storage(x_request_id, object_storage_id, body, x_trace_id=x_trace_id)
        print("The response of ObjectStoragesApi->cancel_object_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->cancel_object_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **object_storage_id** | **str**| The identifier of the object storage. | 
 **body** | **object**|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CancelObjectStorageResponse**](CancelObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the objectstorageId and cancel date. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_storage**
> CreateObjectStorageResponse create_object_storage(x_request_id, create_object_storage_request, x_trace_id=x_trace_id)

Create a new object storage

Create / purchase a new object storage in your account. Please note that you can only buy one object storage per location. You can actually increase the object storage space via `POST` to `/v1/object-storages/{objectStorageId}/resize`

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.create_object_storage_request import CreateObjectStorageRequest
from pfruck_contabo.models.create_object_storage_response import CreateObjectStorageResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_object_storage_request = pfruck_contabo.CreateObjectStorageRequest() # CreateObjectStorageRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create a new object storage
        api_response = api_instance.create_object_storage(x_request_id, create_object_storage_request, x_trace_id=x_trace_id)
        print("The response of ObjectStoragesApi->create_object_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->create_object_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **create_object_storage_request** | [**CreateObjectStorageRequest**](CreateObjectStorageRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateObjectStorageResponse**](CreateObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard object storage attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_center_list**
> ListDataCenterResponse retrieve_data_center_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, slug=slug, name=name, region_name=region_name, region_slug=region_slug)

List data centers

List all data centers and their corresponding regions.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_data_center_response import ListDataCenterResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    slug = 'EU1' # str | Filter as match for data centers. (optional)
    name = 'European Union 1' # str | Filter for Object Storages regions. (optional)
    region_name = 'European Union' # str | Filter for Object Storage region names. (optional)
    region_slug = 'EU' # str | Filter for Object Storage region slugs. (optional)

    try:
        # List data centers
        api_response = api_instance.retrieve_data_center_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, slug=slug, name=name, region_name=region_name, region_slug=region_slug)
        print("The response of ObjectStoragesApi->retrieve_data_center_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->retrieve_data_center_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **slug** | **str**| Filter as match for data centers. | [optional] 
 **name** | **str**| Filter for Object Storages regions. | [optional] 
 **region_name** | **str**| Filter for Object Storage region names. | [optional] 
 **region_slug** | **str**| Filter for Object Storage region slugs. | [optional] 

### Return type

[**ListDataCenterResponse**](ListDataCenterResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of data centers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_storage**
> FindObjectStorageResponse retrieve_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)

Get specific object storage by its id

Get data for a specific object storage on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_object_storage_response import FindObjectStorageResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = '4a6f95be-2ac0-4e3c-8eed-0dc67afed640' # str | The identifier of the object storage.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get specific object storage by its id
        api_response = api_instance.retrieve_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)
        print("The response of ObjectStoragesApi->retrieve_object_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **object_storage_id** | **str**| The identifier of the object storage. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindObjectStorageResponse**](FindObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard object storage attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_storage_list**
> ListObjectStorageResponse retrieve_object_storage_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, data_center_name=data_center_name, s3_tenant_id=s3_tenant_id, region=region, display_name=display_name)

List all your object storages

List and filter all object storages in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_object_storage_response import ListObjectStorageResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    data_center_name = 'European Union 2' # str | Filter for Object Storage locations. (optional)
    s3_tenant_id = '2cd2e5e1444a41b0bed16c6410ecaa84' # str | Filter for Object Storage S3 tenantId. (optional)
    region = 'EU' # str | Filter for Object Storage by regions. Available regions: EU, US-central, SIN (optional)
    display_name = 'MyObjectStorage' # str | Filter for Object Storage by display name. (optional)

    try:
        # List all your object storages
        api_response = api_instance.retrieve_object_storage_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, data_center_name=data_center_name, s3_tenant_id=s3_tenant_id, region=region, display_name=display_name)
        print("The response of ObjectStoragesApi->retrieve_object_storage_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storage_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **data_center_name** | **str**| Filter for Object Storage locations. | [optional] 
 **s3_tenant_id** | **str**| Filter for Object Storage S3 tenantId. | [optional] 
 **region** | **str**| Filter for Object Storage by regions. Available regions: EU, US-central, SIN | [optional] 
 **display_name** | **str**| Filter for Object Storage by display name. | [optional] 

### Return type

[**ListObjectStorageResponse**](ListObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of object storages. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_storages_stats**
> ObjectStoragesStatsResponse retrieve_object_storages_stats(x_request_id, object_storage_id, x_trace_id=x_trace_id)

List usage statistics about the specified object storage

List usage statistics about the specified object storage such as the number of objects uploaded / created, used object storage space. Please note that the usage statistics are updated regularly and are not live usage statistics.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.object_storages_stats_response import ObjectStoragesStatsResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = '4a6f95be-2ac0-4e3c-8eed-0dc67afed640' # str | The identifier of the object storage.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # List usage statistics about the specified object storage
        api_response = api_instance.retrieve_object_storages_stats(x_request_id, object_storage_id, x_trace_id=x_trace_id)
        print("The response of ObjectStoragesApi->retrieve_object_storages_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storages_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **object_storage_id** | **str**| The identifier of the object storage. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ObjectStoragesStatsResponse**](ObjectStoragesStatsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the object storages count the current object storages and give the current quota maximum. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_storage**
> CancelObjectStorageResponse update_object_storage(x_request_id, object_storage_id, patch_object_storage_request, x_trace_id=x_trace_id)

Modifies the display name of object storage

Modifies the display name of object storage. Display name must be unique.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_object_storage_response import CancelObjectStorageResponse
from pfruck_contabo.models.patch_object_storage_request import PatchObjectStorageRequest
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = '4a6f95be-2ac0-4e3c-8eed-0dc67afed640' # str | The identifier of the object storage.
    patch_object_storage_request = pfruck_contabo.PatchObjectStorageRequest() # PatchObjectStorageRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Modifies the display name of object storage
        api_response = api_instance.update_object_storage(x_request_id, object_storage_id, patch_object_storage_request, x_trace_id=x_trace_id)
        print("The response of ObjectStoragesApi->update_object_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->update_object_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **object_storage_id** | **str**| The identifier of the object storage. | 
 **patch_object_storage_request** | [**PatchObjectStorageRequest**](PatchObjectStorageRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CancelObjectStorageResponse**](CancelObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the object storage with updated display name. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_object_storage**
> UpgradeObjectStorageResponse upgrade_object_storage(x_request_id, object_storage_id, upgrade_object_storage_request, x_trace_id=x_trace_id)

Upgrade object storage size resp. update autoscaling settings.

Upgrade object storage size. You can also adjust the autoscaling settings for your object storage. Autoscaling allows you to automatically purchase storage capacity on a monthly basis up to the specified limit.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.upgrade_object_storage_request import UpgradeObjectStorageRequest
from pfruck_contabo.models.upgrade_object_storage_response import UpgradeObjectStorageResponse
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
    api_instance = pfruck_contabo.ObjectStoragesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = '4a6f95be-2ac0-4e3c-8eed-0dc67afed640' # str | The identifier of the object storage.
    upgrade_object_storage_request = pfruck_contabo.UpgradeObjectStorageRequest() # UpgradeObjectStorageRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Upgrade object storage size resp. update autoscaling settings.
        api_response = api_instance.upgrade_object_storage(x_request_id, object_storage_id, upgrade_object_storage_request, x_trace_id=x_trace_id)
        print("The response of ObjectStoragesApi->upgrade_object_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesApi->upgrade_object_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **object_storage_id** | **str**| The identifier of the object storage. | 
 **upgrade_object_storage_request** | [**UpgradeObjectStorageRequest**](UpgradeObjectStorageRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpgradeObjectStorageResponse**](UpgradeObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard object storage attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

