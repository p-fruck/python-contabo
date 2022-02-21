# pfruck_contabo.ObjectStoragesAuditsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_object_storage_audits_list**](ObjectStoragesAuditsApi.md#retrieve_object_storage_audits_list) | **GET** /v1/object-storages/audits | List history about your object storages (audit)

# **retrieve_object_storage_audits_list**
> ListObjectStorageAuditResponse retrieve_object_storage_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, request_id=request_id, changed_by=changed_by)

List history about your object storages (audit)

List and filters the history about your object storages.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ObjectStoragesAuditsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
object_storage_id = 'object_storage_id_example' # str | The identifier of the object storage. (optional)
request_id = 'request_id_example' # str | The requestId of the API call which led to the change. (optional)
changed_by = 'changed_by_example' # str | changedBy of the user which led to the change. (optional)

try:
    # List history about your object storages (audit)
    api_response = api_instance.retrieve_object_storage_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, request_id=request_id, changed_by=changed_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoragesAuditsApi->retrieve_object_storage_audits_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **object_storage_id** | **str**| The identifier of the object storage. | [optional] 
 **request_id** | **str**| The requestId of the API call which led to the change. | [optional] 
 **changed_by** | **str**| changedBy of the user which led to the change. | [optional] 

### Return type

[**ListObjectStorageAuditResponse**](ListObjectStorageAuditResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

