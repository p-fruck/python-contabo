# pfruck_contabo.ObjectStoragesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_object_storage**](ObjectStoragesApi.md#cancel_object_storage) | **PATCH** /v1/object-storages/{objectStorageId}/cancel | Cancels the specified object storage at the next possible date
[**create_object_storage**](ObjectStoragesApi.md#create_object_storage) | **POST** /v1/object-storages | Create a new object storage
[**retrieve_data_center_list**](ObjectStoragesApi.md#retrieve_data_center_list) | **GET** /v1/data-centers | List data centers
[**retrieve_object_storage**](ObjectStoragesApi.md#retrieve_object_storage) | **GET** /v1/object-storages/{objectStorageId} | Get specific object storage by its id
[**retrieve_object_storage_list**](ObjectStoragesApi.md#retrieve_object_storage_list) | **GET** /v1/object-storages | List all your Object Storages
[**retrieve_object_storages_stats**](ObjectStoragesApi.md#retrieve_object_storages_stats) | **GET** /v1/object-storages/{objectStorageId}/stats | List usage statistics about the specified object storage
[**upgrade_object_storage**](ObjectStoragesApi.md#upgrade_object_storage) | **POST** /v1/object-storages/{objectStorageId}/resize | Upgrade object storage size resp. update auto scaling settings.


# **cancel_object_storage**
> CancelObjectStorageResponse cancel_object_storage(x_request_id, object_storage_id)

Cancels the specified object storage at the next possible date

Cancels the specified object storage at the next possible date. Please be aware of your contract periods.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.cancel_object_storage_response import CancelObjectStorageResponse
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = "4a6f95be-2ac0-4e3c-8eed-0dc67afed640" # str | The identifier of the object storage
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Cancels the specified object storage at the next possible date
        api_response = api_instance.cancel_object_storage(x_request_id, object_storage_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->cancel_object_storage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Cancels the specified object storage at the next possible date
        api_response = api_instance.cancel_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->cancel_object_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **object_storage_id** | **str**| The identifier of the object storage |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CancelObjectStorageResponse**](CancelObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the objectstorageId and cancel date. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_storage**
> CreateObjectStorageResponse create_object_storage(x_request_id, create_object_storage_request)

Create a new object storage

Create / purchase a new object storage in your account. Please note that you can only buy one object storage per location. You can actually increase the object storage space via `POST` to `/v1/object-storages/{objectStorageId}/resize`

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.create_object_storage_response import CreateObjectStorageResponse
from pfruck_contabo.model.create_object_storage_request import CreateObjectStorageRequest
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_object_storage_request = CreateObjectStorageRequest(
        region="EU",
        auto_scaling=None,
        total_purchased_space_tb=6,
    ) # CreateObjectStorageRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new object storage
        api_response = api_instance.create_object_storage(x_request_id, create_object_storage_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->create_object_storage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new object storage
        api_response = api_instance.create_object_storage(x_request_id, create_object_storage_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
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
> ListDataCenterResponse retrieve_data_center_list(x_request_id)

List data centers

List all data centers and their corresponding regions.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.list_data_center_response import ListDataCenterResponse
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    slug = "EU1" # str | Filter as match for data centers. (optional)
    name = "European Union (Germany) 1" # str | Filter for Object Storages regions. (optional)
    region_name = "European Union (Germany)" # str | Filter for Object Storage region names. (optional)
    region_slug = "EU" # str | Filter for Object Storage region slugs. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List data centers
        api_response = api_instance.retrieve_data_center_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_data_center_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List data centers
        api_response = api_instance.retrieve_data_center_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, slug=slug, name=name, region_name=region_name, region_slug=region_slug)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_data_center_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
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
> FindObjectStorageResponse retrieve_object_storage(x_request_id, object_storage_id)

Get specific object storage by its id

Get data for a specific object storage on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.find_object_storage_response import FindObjectStorageResponse
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = "4a6f95be-2ac0-4e3c-8eed-0dc67afed640" # str | The identifier of the object storage
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific object storage by its id
        api_response = api_instance.retrieve_object_storage(x_request_id, object_storage_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific object storage by its id
        api_response = api_instance.retrieve_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **object_storage_id** | **str**| The identifier of the object storage |
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
> ListObjectStorageResponse retrieve_object_storage_list(x_request_id)

List all your Object Storages

List and filter all Object Storages in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.list_object_storage_response import ListObjectStorageResponse
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    data_center_name = "EU" # str | Filter for Object Storage locations. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all your Object Storages
        api_response = api_instance.retrieve_object_storage_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storage_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all your Object Storages
        api_response = api_instance.retrieve_object_storage_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, data_center_name=data_center_name)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storage_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **data_center_name** | **str**| Filter for Object Storage locations. | [optional]

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
> ObjectStoragesStatsResponse retrieve_object_storages_stats(x_request_id, object_storage_id)

List usage statistics about the specified object storage

List usage statistics about the specified object storage such as the number of objects uploaded / created, used object storage space. Please note that the usage statistics are updated regularly and are not live usage statistics.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.object_storages_stats_response import ObjectStoragesStatsResponse
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = "4a6f95be-2ac0-4e3c-8eed-0dc67afed640" # str | The identifier of the object storage
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List usage statistics about the specified object storage
        api_response = api_instance.retrieve_object_storages_stats(x_request_id, object_storage_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storages_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List usage statistics about the specified object storage
        api_response = api_instance.retrieve_object_storages_stats(x_request_id, object_storage_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->retrieve_object_storages_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **object_storage_id** | **str**| The identifier of the object storage |
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

# **upgrade_object_storage**
> UpdateObjectStorageResponse upgrade_object_storage(x_request_id, object_storage_id, upgrade_object_storage_request)

Upgrade object storage size resp. update auto scaling settings.

Upgrade object storage size. You can also adjust the auto scaling settings for your object storage. Auto-scaling allows you to automatically purchase storage capacity on a monthly basis up to the specified limit.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import object_storages_api
from pfruck_contabo.model.upgrade_object_storage_request import UpgradeObjectStorageRequest
from pfruck_contabo.model.update_object_storage_response import UpdateObjectStorageResponse
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
    api_instance = object_storages_api.ObjectStoragesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    object_storage_id = "4a6f95be-2ac0-4e3c-8eed-0dc67afed640" # str | The identifier of the object storage
    upgrade_object_storage_request = UpgradeObjectStorageRequest(
        auto_scaling=None,
        total_purchased_space_tb=8,
    ) # UpgradeObjectStorageRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upgrade object storage size resp. update auto scaling settings.
        api_response = api_instance.upgrade_object_storage(x_request_id, object_storage_id, upgrade_object_storage_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->upgrade_object_storage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upgrade object storage size resp. update auto scaling settings.
        api_response = api_instance.upgrade_object_storage(x_request_id, object_storage_id, upgrade_object_storage_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ObjectStoragesApi->upgrade_object_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **object_storage_id** | **str**| The identifier of the object storage |
 **upgrade_object_storage_request** | [**UpgradeObjectStorageRequest**](UpgradeObjectStorageRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**UpdateObjectStorageResponse**](UpdateObjectStorageResponse.md)

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

