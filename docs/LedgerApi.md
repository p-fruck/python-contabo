# pfruck_contabo.LedgerApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_ledger_entries_list**](LedgerApi.md#retrieve_ledger_entries_list) | **GET** /v1/ledger/ledger-entries | List ledger entries


# **retrieve_ledger_entries_list**
> ListLedgerEntriesReponse retrieve_ledger_entries_list(x_request_id)

List ledger entries

List all transactions for your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import ledger_api
from pfruck_contabo.model.list_ledger_entries_reponse import ListLedgerEntriesReponse
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
    api_instance = ledger_api.LedgerApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    transaction_start_date = "2020-09-01" # str | Start date of the interval in which you want to see the transactions (optional)
    transaction_end_date = "2020-09-30" # str | Start date of the interval in which you want to see the transactions (optional)

    # example passing only required values which don't have defaults set
    try:
        # List ledger entries
        api_response = api_instance.retrieve_ledger_entries_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling LedgerApi->retrieve_ledger_entries_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ledger entries
        api_response = api_instance.retrieve_ledger_entries_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, transaction_start_date=transaction_start_date, transaction_end_date=transaction_end_date)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling LedgerApi->retrieve_ledger_entries_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **transaction_start_date** | **str**| Start date of the interval in which you want to see the transactions | [optional]
 **transaction_end_date** | **str**| Start date of the interval in which you want to see the transactions | [optional]

### Return type

[**ListLedgerEntriesReponse**](ListLedgerEntriesReponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of ledger entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

