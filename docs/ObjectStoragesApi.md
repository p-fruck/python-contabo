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
> CancelObjectStorageResponse cancel_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)

Cancels the specified object storage at the next possible date

Cancels the specified object storage at the next possible date. Please be aware of your contract periods.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
object_storage_id = 'object_storage_id_example' # str | The identifier of the object storage
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Cancels the specified object storage at the next possible date
    api_response = api_instance.cancel_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_storage**
> CreateObjectStorageResponse create_object_storage(body, x_request_id, x_trace_id=x_trace_id)

Create a new object storage

Create / purchase a new object storage in your account. Please note that you can only buy one object storage per location. You can actually increase the object storage space via `POST` to `/v1/object-storages/{objectStorageId}/resize`

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateObjectStorageRequest() # CreateObjectStorageRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new object storage
    api_response = api_instance.create_object_storage(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoragesApi->create_object_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateObjectStorageRequest**](CreateObjectStorageRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateObjectStorageResponse**](CreateObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_center_list**
> ListDataCenterResponse retrieve_data_center_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, slug=slug, name=name, region_name=region_name, region_slug=region_slug)

List data centers

List all data centers and their corresponding regions.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
slug = 'slug_example' # str | Filter as match for data centers. (optional)
name = 'name_example' # str | Filter for Object Storages regions. (optional)
region_name = 'region_name_example' # str | Filter for Object Storage region names. (optional)
region_slug = 'region_slug_example' # str | Filter for Object Storage region slugs. (optional)

try:
    # List data centers
    api_response = api_instance.retrieve_data_center_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, slug=slug, name=name, region_name=region_name, region_slug=region_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoragesApi->retrieve_data_center_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_storage**
> FindObjectStorageResponse retrieve_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)

Get specific object storage by its id

Get data for a specific object storage on your account.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
object_storage_id = 'object_storage_id_example' # str | The identifier of the object storage
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get specific object storage by its id
    api_response = api_instance.retrieve_object_storage(x_request_id, object_storage_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_storage_list**
> ListObjectStorageResponse retrieve_object_storage_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, data_center_name=data_center_name)

List all your Object Storages

List and filter all Object Storages in your account

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
data_center_name = 'data_center_name_example' # str | Filter for Object Storage locations. (optional)

try:
    # List all your Object Storages
    api_response = api_instance.retrieve_object_storage_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, data_center_name=data_center_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoragesApi->retrieve_object_storage_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **data_center_name** | **str**| Filter for Object Storage locations. | [optional] 

### Return type

[**ListObjectStorageResponse**](ListObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_object_storages_stats**
> ObjectStoragesStatsResponse retrieve_object_storages_stats(x_request_id, object_storage_id, x_trace_id=x_trace_id)

List usage statistics about the specified object storage

List usage statistics about the specified object storage such as the number of objects uploaded / created, used object storage space. Please note that the usage statistics are updated regularly and are not live usage statistics.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
object_storage_id = 'object_storage_id_example' # str | The identifier of the object storage
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # List usage statistics about the specified object storage
    api_response = api_instance.retrieve_object_storages_stats(x_request_id, object_storage_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_object_storage**
> UpdateObjectStorageResponse upgrade_object_storage(body, x_request_id, object_storage_id, x_trace_id=x_trace_id)

Upgrade object storage size resp. update auto scaling settings.

Upgrade object storage size. You can also adjust the auto scaling settings for your object storage. Auto-scaling allows you to automatically purchase storage capacity on a monthly basis up to the specified limit.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpgradeObjectStorageRequest() # UpgradeObjectStorageRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
object_storage_id = 'object_storage_id_example' # str | The identifier of the object storage
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Upgrade object storage size resp. update auto scaling settings.
    api_response = api_instance.upgrade_object_storage(body, x_request_id, object_storage_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoragesApi->upgrade_object_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeObjectStorageRequest**](UpgradeObjectStorageRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **object_storage_id** | **str**| The identifier of the object storage | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpdateObjectStorageResponse**](UpdateObjectStorageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

