# pfruck_contabo.ObjectStoragesAuditsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_object_storage_audits_list**](ObjectStoragesAuditsApi.md#retrieve_object_storage_audits_list) | **GET** /v1/object-storages/audits | List history about your object storages (audit)


# **retrieve_object_storage_audits_list**
> ListObjectStorageAuditResponse retrieve_object_storage_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, request_id=request_id, changed_by=changed_by, start_date=start_date, end_date=end_date)

List history about your object storages (audit)

List and filters the history about your object storages.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_object_storage_audit_response import ListObjectStorageAuditResponse
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
    api_instance = pfruck_contabo.ObjectStoragesAuditsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    object_storage_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the object storage. (optional)
    request_id = 'D5FD9FAF-58C0-4406-8F46-F449B8E4FEC3' # str | The requestId of the API call which led to the change. (optional)
    changed_by = '23cbb6d6-cb11-4330-bdff-7bb791df2e23' # str | changedBy of the user which led to the change. (optional)
    start_date = '2021-01-01' # date | Start of search time range. (optional)
    end_date = '2021-01-01' # date | End of search time range. (optional)

    try:
        # List history about your object storages (audit)
        api_response = api_instance.retrieve_object_storage_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, request_id=request_id, changed_by=changed_by, start_date=start_date, end_date=end_date)
        print("The response of ObjectStoragesAuditsApi->retrieve_object_storage_audits_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStoragesAuditsApi->retrieve_object_storage_audits_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **object_storage_id** | **str**| The identifier of the object storage. | [optional] 
 **request_id** | **str**| The requestId of the API call which led to the change. | [optional] 
 **changed_by** | **str**| changedBy of the user which led to the change. | [optional] 
 **start_date** | **date**| Start of search time range. | [optional] 
 **end_date** | **date**| End of search time range. | [optional] 

### Return type

[**ListObjectStorageAuditResponse**](ListObjectStorageAuditResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of object storage audits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

