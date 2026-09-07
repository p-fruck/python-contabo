# pfruck_contabo.HandlesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_handle**](HandlesApi.md#create_handle) | **POST** /v1/domains/handles | Create specific handle
[**list_handles**](HandlesApi.md#list_handles) | **GET** /v1/domains/handles | List all handles
[**remove_handle**](HandlesApi.md#remove_handle) | **DELETE** /v1/domains/handles/{handleId} | Remove specific handle
[**retrieve_handle**](HandlesApi.md#retrieve_handle) | **GET** /v1/domains/handles/{handleId} | Get specific handle
[**set_default_handle**](HandlesApi.md#set_default_handle) | **PATCH** /v1/domains/handles/{handleId}/default | Set default handle
[**update_handle**](HandlesApi.md#update_handle) | **PUT** /v1/domains/handles/{handleId} | Update specific handle


# **create_handle**
> HandleCreateResponse create_handle(x_request_id, handle_create_request, x_trace_id=x_trace_id)

Create specific handle

Create specific handle

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.handle_create_request import HandleCreateRequest
from pfruck_contabo.models.handle_create_response import HandleCreateResponse
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
    api_instance = pfruck_contabo.HandlesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    handle_create_request = pfruck_contabo.HandleCreateRequest() # HandleCreateRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create specific handle
        api_response = api_instance.create_handle(x_request_id, handle_create_request, x_trace_id=x_trace_id)
        print("The response of HandlesApi->create_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlesApi->create_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **handle_create_request** | [**HandleCreateRequest**](HandleCreateRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**HandleCreateResponse**](HandleCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard handle attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_handles**
> HandleListResponse list_handles(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, show_defaults=show_defaults, search=search, countries=countries, handle_type=handle_type, first_name=first_name, last_name=last_name)

List all handles

List and filter all your handles

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.handle_list_response import HandleListResponse
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
    api_instance = pfruck_contabo.HandlesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = 'MyHandle' # str | Filter as substring match for handle name. (optional)
    show_defaults = true # bool | Filter handles to show or not the public handles (optional)
    search = 'hello' # str | full text search on handles on handleid, organization name, handlename  (optional)
    countries = 'DE,US' # str | list of country codes to filter handles that are available in these countries (comma separated) (optional)
    handle_type = 'person' # str | Filter handles by type, e.g. person, organization. (optional)
    first_name = 'FirstName' # str | Filter handles by first name. (optional)
    last_name = 'LastName' # str | Filter handles by last name. (optional)

    try:
        # List all handles
        api_response = api_instance.list_handles(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, show_defaults=show_defaults, search=search, countries=countries, handle_type=handle_type, first_name=first_name, last_name=last_name)
        print("The response of HandlesApi->list_handles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlesApi->list_handles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| Filter as substring match for handle name. | [optional] 
 **show_defaults** | **bool**| Filter handles to show or not the public handles | [optional] 
 **search** | **str**| full text search on handles on handleid, organization name, handlename  | [optional] 
 **countries** | **str**| list of country codes to filter handles that are available in these countries (comma separated) | [optional] 
 **handle_type** | **str**| Filter handles by type, e.g. person, organization. | [optional] 
 **first_name** | **str**| Filter handles by first name. | [optional] 
 **last_name** | **str**| Filter handles by last name. | [optional] 

### Return type

[**HandleListResponse**](HandleListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard handles attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_handle**
> remove_handle(x_request_id, handle_id, x_trace_id=x_trace_id)

Remove specific handle

Remove specific handle

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.HandlesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    handle_id = 'CA123O1' # str | The identifier of the handle
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Remove specific handle
        api_instance.remove_handle(x_request_id, handle_id, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling HandlesApi->remove_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **handle_id** | **str**| The identifier of the handle | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body has no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_handle**
> HandleFindResponse retrieve_handle(x_request_id, handle_id, x_trace_id=x_trace_id)

Get specific handle

Get specific handle

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.handle_find_response import HandleFindResponse
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
    api_instance = pfruck_contabo.HandlesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    handle_id = 'CA123O1' # str | The identifier of the handle
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get specific handle
        api_response = api_instance.retrieve_handle(x_request_id, handle_id, x_trace_id=x_trace_id)
        print("The response of HandlesApi->retrieve_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlesApi->retrieve_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **handle_id** | **str**| The identifier of the handle | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**HandleFindResponse**](HandleFindResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard handle attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_handle**
> SetDefaultHandleResponse set_default_handle(x_request_id, handle_id, x_trace_id=x_trace_id)

Set default handle

Set default handle

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.set_default_handle_response import SetDefaultHandleResponse
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
    api_instance = pfruck_contabo.HandlesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    handle_id = 'CA123O1' # str | The identifier of the handle
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Set default handle
        api_response = api_instance.set_default_handle(x_request_id, handle_id, x_trace_id=x_trace_id)
        print("The response of HandlesApi->set_default_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlesApi->set_default_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **handle_id** | **str**| The identifier of the handle | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**SetDefaultHandleResponse**](SetDefaultHandleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a details of a handle. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_handle**
> HandlePatchResponse update_handle(x_request_id, handle_id, handle_patch_request, x_trace_id=x_trace_id)

Update specific handle

Update specific handle

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.handle_patch_request import HandlePatchRequest
from pfruck_contabo.models.handle_patch_response import HandlePatchResponse
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
    api_instance = pfruck_contabo.HandlesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    handle_id = 'CA123O1' # str | The identifier of the handle
    handle_patch_request = pfruck_contabo.HandlePatchRequest() # HandlePatchRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update specific handle
        api_response = api_instance.update_handle(x_request_id, handle_id, handle_patch_request, x_trace_id=x_trace_id)
        print("The response of HandlesApi->update_handle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HandlesApi->update_handle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **handle_id** | **str**| The identifier of the handle | 
 **handle_patch_request** | [**HandlePatchRequest**](HandlePatchRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**HandlePatchResponse**](HandlePatchResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

