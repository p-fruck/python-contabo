# pfruck_contabo.CheckCollectionsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_ext_check_collection**](CheckCollectionsApi.md#cancel_ext_check_collection) | **PATCH** /v1/troubleshooting/check-collections/{checkCollectionId} | Cancel check collection
[**get_ext_check_collection**](CheckCollectionsApi.md#get_ext_check_collection) | **GET** /v1/troubleshooting/check-collections/{checkCollectionId} | Get check collection
[**list_ext_check_collections**](CheckCollectionsApi.md#list_ext_check_collections) | **GET** /v1/troubleshooting/check-collections | List check collections
[**start_ext_check_collection**](CheckCollectionsApi.md#start_ext_check_collection) | **POST** /v1/troubleshooting/check-collections | Start check collection


# **cancel_ext_check_collection**
> ExtCheckCollectionsGetResponse cancel_ext_check_collection(x_request_id, check_collection_id, cancel_request, x_trace_id=x_trace_id)

Cancel check collection

Cancel check collection

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_request import CancelRequest
from pfruck_contabo.models.ext_check_collections_get_response import ExtCheckCollectionsGetResponse
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
    api_instance = pfruck_contabo.CheckCollectionsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    check_collection_id = 12345 # float | Check collection's id
    cancel_request = pfruck_contabo.CancelRequest() # CancelRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Cancel check collection
        api_response = api_instance.cancel_ext_check_collection(x_request_id, check_collection_id, cancel_request, x_trace_id=x_trace_id)
        print("The response of CheckCollectionsApi->cancel_ext_check_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckCollectionsApi->cancel_ext_check_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **check_collection_id** | **float**| Check collection&#39;s id | 
 **cancel_request** | [**CancelRequest**](CancelRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtCheckCollectionsGetResponse**](ExtCheckCollectionsGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancelled check collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ext_check_collection**
> ExtCheckCollectionsGetResponse get_ext_check_collection(x_request_id, check_collection_id, x_trace_id=x_trace_id, exclude_check_statuses=exclude_check_statuses)

Get check collection

Get a single check collection by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_check_collections_get_response import ExtCheckCollectionsGetResponse
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
    api_instance = pfruck_contabo.CheckCollectionsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    check_collection_id = 12345 # float | Check collection's id
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    exclude_check_statuses = ['[\"skipped\",\"cancelled\"]'] # List[str] | Check statuses to exclude (optional)

    try:
        # Get check collection
        api_response = api_instance.get_ext_check_collection(x_request_id, check_collection_id, x_trace_id=x_trace_id, exclude_check_statuses=exclude_check_statuses)
        print("The response of CheckCollectionsApi->get_ext_check_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckCollectionsApi->get_ext_check_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **check_collection_id** | **float**| Check collection&#39;s id | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **exclude_check_statuses** | [**List[str]**](str.md)| Check statuses to exclude | [optional] 

### Return type

[**ExtCheckCollectionsGetResponse**](ExtCheckCollectionsGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single check collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ext_check_collections**
> ExtCheckCollectionsListResponse list_ext_check_collections(x_request_id, x_trace_id=x_trace_id, object_type=object_type, object_id=object_id, check_collection_template_id=check_collection_template_id, exclude_check_statuses=exclude_check_statuses, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)

List check collections

List and filter all check collections

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_check_collections_list_response import ExtCheckCollectionsListResponse
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
    api_instance = pfruck_contabo.CheckCollectionsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    object_type = 'vserver' # str | Object type to be handled (optional)
    object_id = '4711' # str | ID of the object, to be handled (optional)
    check_collection_template_id = 12345 # float | Check Collection Template for this check collection (optional)
    exclude_check_statuses = ['[\"skipped\",\"cancelled\"]'] # List[str] | Check statuses to exclude (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    creation_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for created date (optional)
    creation_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for created date (optional)
    modification_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for modified date (optional)
    modification_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for modified date (optional)

    try:
        # List check collections
        api_response = api_instance.list_ext_check_collections(x_request_id, x_trace_id=x_trace_id, object_type=object_type, object_id=object_id, check_collection_template_id=check_collection_template_id, exclude_check_statuses=exclude_check_statuses, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)
        print("The response of CheckCollectionsApi->list_ext_check_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckCollectionsApi->list_ext_check_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **object_type** | **str**| Object type to be handled | [optional] 
 **object_id** | **str**| ID of the object, to be handled | [optional] 
 **check_collection_template_id** | **float**| Check Collection Template for this check collection | [optional] 
 **exclude_check_statuses** | [**List[str]**](str.md)| Check statuses to exclude | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **creation_start_time** | **datetime**| Start of search time range for created date | [optional] 
 **creation_end_time** | **datetime**| End of search time range for created date | [optional] 
 **modification_start_time** | **datetime**| Start of search time range for modified date | [optional] 
 **modification_end_time** | **datetime**| End of search time range for modified date | [optional] 

### Return type

[**ExtCheckCollectionsListResponse**](ExtCheckCollectionsListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of check collections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ext_check_collection**
> ExtCheckCollectionsGetResponse start_ext_check_collection(x_request_id, base_check_collection_create_request, x_trace_id=x_trace_id)

Start check collection

Start a new check collection

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.base_check_collection_create_request import BaseCheckCollectionCreateRequest
from pfruck_contabo.models.ext_check_collections_get_response import ExtCheckCollectionsGetResponse
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
    api_instance = pfruck_contabo.CheckCollectionsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    base_check_collection_create_request = pfruck_contabo.BaseCheckCollectionCreateRequest() # BaseCheckCollectionCreateRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Start check collection
        api_response = api_instance.start_ext_check_collection(x_request_id, base_check_collection_create_request, x_trace_id=x_trace_id)
        print("The response of CheckCollectionsApi->start_ext_check_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckCollectionsApi->start_ext_check_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **base_check_collection_create_request** | [**BaseCheckCollectionCreateRequest**](BaseCheckCollectionCreateRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtCheckCollectionsGetResponse**](ExtCheckCollectionsGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Started check collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

