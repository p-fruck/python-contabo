# pfruck_contabo.InstancesAuditsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_instances_audits_list**](InstancesAuditsApi.md#retrieve_instances_audits_list) | **GET** /v1/compute/instances/audits | List history about your instances (audit) triggered via the API

# **retrieve_instances_audits_list**
> ListInstancesAuditResponse retrieve_instances_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, instance_id=instance_id, request_id=request_id, changed_by=changed_by)

List history about your instances (audit) triggered via the API

List and filters the history about your instances your triggered via the API.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InstancesAuditsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
instance_id = 789 # int | The identifier of the instances. (optional)
request_id = 'request_id_example' # str | The requestId of the API call which led to the change. (optional)
changed_by = 'changed_by_example' # str | changedBy of the user which led to the change. (optional)

try:
    # List history about your instances (audit) triggered via the API
    api_response = api_instance.retrieve_instances_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, instance_id=instance_id, request_id=request_id, changed_by=changed_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesAuditsApi->retrieve_instances_audits_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **instance_id** | **int**| The identifier of the instances. | [optional] 
 **request_id** | **str**| The requestId of the API call which led to the change. | [optional] 
 **changed_by** | **str**| changedBy of the user which led to the change. | [optional] 

### Return type

[**ListInstancesAuditResponse**](ListInstancesAuditResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

