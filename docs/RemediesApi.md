# pfruck_contabo.RemediesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_ext_remedy**](RemediesApi.md#cancel_ext_remedy) | **PATCH** /v1/troubleshooting/remedies/{remedyId} | Cancel remedy
[**get_ext_remedy**](RemediesApi.md#get_ext_remedy) | **GET** /v1/troubleshooting/remedies/{remedyId} | Get remedy
[**list_ext_remedies**](RemediesApi.md#list_ext_remedies) | **GET** /v1/troubleshooting/remedies | List remedy
[**start_ext_remedy**](RemediesApi.md#start_ext_remedy) | **POST** /v1/troubleshooting/remedies | Start remedy


# **cancel_ext_remedy**
> ExtRemediesGetResponse cancel_ext_remedy(x_request_id, remedy_id, cancel_request, x_trace_id=x_trace_id)

Cancel remedy

Cancel remedy

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_request import CancelRequest
from pfruck_contabo.models.ext_remedies_get_response import ExtRemediesGetResponse
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
    api_instance = pfruck_contabo.RemediesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    remedy_id = 12345 # float | Remedy's id
    cancel_request = pfruck_contabo.CancelRequest() # CancelRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Cancel remedy
        api_response = api_instance.cancel_ext_remedy(x_request_id, remedy_id, cancel_request, x_trace_id=x_trace_id)
        print("The response of RemediesApi->cancel_ext_remedy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemediesApi->cancel_ext_remedy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **remedy_id** | **float**| Remedy&#39;s id | 
 **cancel_request** | [**CancelRequest**](CancelRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtRemediesGetResponse**](ExtRemediesGetResponse.md)

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

# **get_ext_remedy**
> ExtRemediesGetResponse get_ext_remedy(x_request_id, remedy_id, x_trace_id=x_trace_id)

Get remedy

Get a single remedy by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_remedies_get_response import ExtRemediesGetResponse
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
    api_instance = pfruck_contabo.RemediesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    remedy_id = 12345 # float | Remedy's id
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get remedy
        api_response = api_instance.get_ext_remedy(x_request_id, remedy_id, x_trace_id=x_trace_id)
        print("The response of RemediesApi->get_ext_remedy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemediesApi->get_ext_remedy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **remedy_id** | **float**| Remedy&#39;s id | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtRemediesGetResponse**](ExtRemediesGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single remedy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ext_remedies**
> ExtRemediesListResponse list_ext_remedies(x_request_id, x_trace_id=x_trace_id, object_type=object_type, object_id=object_id, status=status, remedy_collection_id=remedy_collection_id, remedy_template_id=remedy_template_id, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)

List remedy

List and filter all remedy

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_remedies_list_response import ExtRemediesListResponse
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
    api_instance = pfruck_contabo.RemediesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    object_type = 'vserver' # str | Object type to be handled (optional)
    object_id = '4711' # str | ID of the object, to be handled (optional)
    status = 'failed' # str | Status of the handle (optional)
    remedy_collection_id = 12345 # float | ID of remedy collection if started in scope of a collection (optional)
    remedy_template_id = 12345 # float | Remedy Template for this check (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    creation_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for created date (optional)
    creation_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for created date (optional)
    modification_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for modified date (optional)
    modification_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for modified date (optional)

    try:
        # List remedy
        api_response = api_instance.list_ext_remedies(x_request_id, x_trace_id=x_trace_id, object_type=object_type, object_id=object_id, status=status, remedy_collection_id=remedy_collection_id, remedy_template_id=remedy_template_id, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)
        print("The response of RemediesApi->list_ext_remedies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemediesApi->list_ext_remedies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **object_type** | **str**| Object type to be handled | [optional] 
 **object_id** | **str**| ID of the object, to be handled | [optional] 
 **status** | **str**| Status of the handle | [optional] 
 **remedy_collection_id** | **float**| ID of remedy collection if started in scope of a collection | [optional] 
 **remedy_template_id** | **float**| Remedy Template for this check | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **creation_start_time** | **datetime**| Start of search time range for created date | [optional] 
 **creation_end_time** | **datetime**| End of search time range for created date | [optional] 
 **modification_start_time** | **datetime**| Start of search time range for modified date | [optional] 
 **modification_end_time** | **datetime**| End of search time range for modified date | [optional] 

### Return type

[**ExtRemediesListResponse**](ExtRemediesListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of remedy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ext_remedy**
> ExtRemediesGetResponse start_ext_remedy(x_request_id, base_remedy_create_request, x_trace_id=x_trace_id)

Start remedy

Start a new remedy

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.base_remedy_create_request import BaseRemedyCreateRequest
from pfruck_contabo.models.ext_remedies_get_response import ExtRemediesGetResponse
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
    api_instance = pfruck_contabo.RemediesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    base_remedy_create_request = pfruck_contabo.BaseRemedyCreateRequest() # BaseRemedyCreateRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Start remedy
        api_response = api_instance.start_ext_remedy(x_request_id, base_remedy_create_request, x_trace_id=x_trace_id)
        print("The response of RemediesApi->start_ext_remedy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemediesApi->start_ext_remedy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **base_remedy_create_request** | [**BaseRemedyCreateRequest**](BaseRemedyCreateRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtRemediesGetResponse**](ExtRemediesGetResponse.md)

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

