# pfruck_contabo.ChecksApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_ext_check**](ChecksApi.md#cancel_ext_check) | **PATCH** /v1/troubleshooting/checks/{checkId} | Cancel check
[**get_ext_check**](ChecksApi.md#get_ext_check) | **GET** /v1/troubleshooting/checks/{checkId} | Get check
[**list_ext_checks**](ChecksApi.md#list_ext_checks) | **GET** /v1/troubleshooting/checks | List check
[**start_ext_check**](ChecksApi.md#start_ext_check) | **POST** /v1/troubleshooting/checks | Start check


# **cancel_ext_check**
> ExtChecksGetResponse cancel_ext_check(x_request_id, check_id, cancel_request, x_trace_id=x_trace_id)

Cancel check

Cancel check

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_request import CancelRequest
from pfruck_contabo.models.ext_checks_get_response import ExtChecksGetResponse
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
    api_instance = pfruck_contabo.ChecksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    check_id = 12345 # float | Check's id
    cancel_request = pfruck_contabo.CancelRequest() # CancelRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Cancel check
        api_response = api_instance.cancel_ext_check(x_request_id, check_id, cancel_request, x_trace_id=x_trace_id)
        print("The response of ChecksApi->cancel_ext_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->cancel_ext_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **check_id** | **float**| Check&#39;s id | 
 **cancel_request** | [**CancelRequest**](CancelRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtChecksGetResponse**](ExtChecksGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancelled object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ext_check**
> ExtChecksGetResponse get_ext_check(x_request_id, check_id, x_trace_id=x_trace_id)

Get check

Get a single check by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_checks_get_response import ExtChecksGetResponse
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
    api_instance = pfruck_contabo.ChecksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    check_id = 12345 # float | Check's id
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get check
        api_response = api_instance.get_ext_check(x_request_id, check_id, x_trace_id=x_trace_id)
        print("The response of ChecksApi->get_ext_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->get_ext_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **check_id** | **float**| Check&#39;s id | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtChecksGetResponse**](ExtChecksGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ext_checks**
> ExtChecksListResponse list_ext_checks(x_request_id, x_trace_id=x_trace_id, object_type=object_type, object_id=object_id, status=status, check_collection_id=check_collection_id, check_template_id=check_template_id, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)

List check

List and filter all check

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_checks_list_response import ExtChecksListResponse
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
    api_instance = pfruck_contabo.ChecksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    object_type = 'vserver' # str | Object type to be handled (optional)
    object_id = '4711' # str | ID of the object, to be handled (optional)
    status = 'failed' # str | Status of the handle (optional)
    check_collection_id = 12345 # float | ID of check collection if started in scope of a collection (optional)
    check_template_id = 12345 # float | Check Template for this check (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    creation_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for created date (optional)
    creation_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for created date (optional)
    modification_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for modified date (optional)
    modification_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for modified date (optional)

    try:
        # List check
        api_response = api_instance.list_ext_checks(x_request_id, x_trace_id=x_trace_id, object_type=object_type, object_id=object_id, status=status, check_collection_id=check_collection_id, check_template_id=check_template_id, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)
        print("The response of ChecksApi->list_ext_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->list_ext_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **object_type** | **str**| Object type to be handled | [optional] 
 **object_id** | **str**| ID of the object, to be handled | [optional] 
 **status** | **str**| Status of the handle | [optional] 
 **check_collection_id** | **float**| ID of check collection if started in scope of a collection | [optional] 
 **check_template_id** | **float**| Check Template for this check | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **creation_start_time** | **datetime**| Start of search time range for created date | [optional] 
 **creation_end_time** | **datetime**| End of search time range for created date | [optional] 
 **modification_start_time** | **datetime**| Start of search time range for modified date | [optional] 
 **modification_end_time** | **datetime**| End of search time range for modified date | [optional] 

### Return type

[**ExtChecksListResponse**](ExtChecksListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ext_check**
> ExtChecksGetResponse start_ext_check(x_request_id, base_check_create_request, x_trace_id=x_trace_id)

Start check

Start a new check

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.base_check_create_request import BaseCheckCreateRequest
from pfruck_contabo.models.ext_checks_get_response import ExtChecksGetResponse
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
    api_instance = pfruck_contabo.ChecksApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    base_check_create_request = pfruck_contabo.BaseCheckCreateRequest() # BaseCheckCreateRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Start check
        api_response = api_instance.start_ext_check(x_request_id, base_check_create_request, x_trace_id=x_trace_id)
        print("The response of ChecksApi->start_ext_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->start_ext_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **base_check_create_request** | [**BaseCheckCreateRequest**](BaseCheckCreateRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtChecksGetResponse**](ExtChecksGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Started object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

