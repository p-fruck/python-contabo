# pfruck_contabo.SnapshotsApi

All URIs are relative to *https://api.contabo.intra*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots | Create a new instance snapshot
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Delete existing snapshot by id
[**retrieve_snapshot**](SnapshotsApi.md#retrieve_snapshot) | **GET** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Retrieve a specific snapshot by id
[**retrieve_snapshot_list**](SnapshotsApi.md#retrieve_snapshot_list) | **GET** /v1/compute/instances/{instanceId}/snapshots | List snapshots
[**rollback_snapshot**](SnapshotsApi.md#rollback_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots/{snapshotId}/rollback | Rollback the instance to a specific snapshot by id
[**update_snapshot**](SnapshotsApi.md#update_snapshot) | **PATCH** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Update specific snapshot by id

# **create_snapshot**
> CreateSnapshotResponse create_snapshot(body, x_request_id, instance_id, x_trace_id=x_trace_id)

Create a new instance snapshot

Create a new snapshot for instance, with name and description attributes

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SnapshotsApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateSnapshotRequest() # CreateSnapshotRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new instance snapshot
    api_response = api_instance.create_snapshot(body, x_request_id, instance_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateSnapshotResponse**](CreateSnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot**
> delete_snapshot(x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)

Delete existing snapshot by id

Delete existing instance snapshot by id

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SnapshotsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
snapshot_id = 'snapshot_id_example' # str | The identifier of the snapshot
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete existing snapshot by id
    api_instance.delete_snapshot(x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)
except ApiException as e:
    print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **snapshot_id** | **str**| The identifier of the snapshot | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_snapshot**
> FindSnapshotResponse retrieve_snapshot(x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)

Retrieve a specific snapshot by id

Get all attributes for a specific snapshot

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SnapshotsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
snapshot_id = 'snapshot_id_example' # str | The identifier of the snapshot
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Retrieve a specific snapshot by id
    api_response = api_instance.retrieve_snapshot(x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->retrieve_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **snapshot_id** | **str**| The identifier of the snapshot | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindSnapshotResponse**](FindSnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_snapshot_list**
> ListSnapshotResponse retrieve_snapshot_list(x_request_id, instance_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name)

List snapshots

List and filter all your snapshots for a specific instance

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SnapshotsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
name = 'name_example' # str | Filter as substring match for snapshots names. (optional)

try:
    # List snapshots
    api_response = api_instance.retrieve_snapshot_list(x_request_id, instance_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->retrieve_snapshot_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| Filter as substring match for snapshots names. | [optional] 

### Return type

[**ListSnapshotResponse**](ListSnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_snapshot**
> RollbackSnapshotResponse rollback_snapshot(x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)

Rollback the instance to a specific snapshot by id

Rollback instance to a specific snapshot. The snapshot must be the latest one in order to be able to restore it, otherwise you will receive an error informing you that the snapshot is not the latest

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SnapshotsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
snapshot_id = 'snapshot_id_example' # str | The identifier of the snapshot
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Rollback the instance to a specific snapshot by id
    api_response = api_instance.rollback_snapshot(x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->rollback_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **snapshot_id** | **str**| The identifier of the snapshot | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**RollbackSnapshotResponse**](RollbackSnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot**
> UpdateSnapshotResponse update_snapshot(body, x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)

Update specific snapshot by id

Update attributes of a snapshot. You may only specify the attributes you want to change. If an attribute is not set, it will retain its original value.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SnapshotsApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpdateSnapshotRequest() # UpdateSnapshotRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
instance_id = 789 # int | The identifier of the instance
snapshot_id = 'snapshot_id_example' # str | The identifier of the snapshot
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Update specific snapshot by id
    api_response = api_instance.update_snapshot(body, x_request_id, instance_id, snapshot_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->update_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSnapshotRequest**](UpdateSnapshotRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **snapshot_id** | **str**| The identifier of the snapshot | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpdateSnapshotResponse**](UpdateSnapshotResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

