# pfruck_contabo.DpaAuditsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_dpa_audits_list**](DpaAuditsApi.md#retrieve_dpa_audits_list) | **GET** /v1/dpas/audits | List history about your Dpas (audit)


# **retrieve_dpa_audits_list**
> ListDpaAuditResponse retrieve_dpa_audits_list(x_request_id)

List history about your Dpas (audit)

List and filters the history about your Dpas.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpa_audits_api
from pfruck_contabo.model.list_dpa_audit_response import ListDpaAuditResponse
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
    api_instance = dpa_audits_api.DpaAuditsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    dpa_id = "1b943b25a-c8b5-4570-9135-4bbaa7615b812345" # str | The identifier of the Dpa. (optional)
    request_id = "D5FD9FAF-58C0-4406-8F46-F449B8E4FEC3" # str | The requestId of the API call which led to the change. (optional)
    changed_by = "23cbb6d6-cb11-4330-bdff-7bb791df2e23" # str | User name which did the change. (optional)
    start_date = dateutil_parser('2021-01-01').date() # date | Start of search time range. (optional)
    end_date = dateutil_parser('2021-01-01').date() # date | End of search time range. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List history about your Dpas (audit)
        api_response = api_instance.retrieve_dpa_audits_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DpaAuditsApi->retrieve_dpa_audits_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List history about your Dpas (audit)
        api_response = api_instance.retrieve_dpa_audits_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, dpa_id=dpa_id, request_id=request_id, changed_by=changed_by, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DpaAuditsApi->retrieve_dpa_audits_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **dpa_id** | **str**| The identifier of the Dpa. | [optional]
 **request_id** | **str**| The requestId of the API call which led to the change. | [optional]
 **changed_by** | **str**| User name which did the change. | [optional]
 **start_date** | **date**| Start of search time range. | [optional]
 **end_date** | **date**| End of search time range. | [optional]

### Return type

[**ListDpaAuditResponse**](ListDpaAuditResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of Dpa audits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

