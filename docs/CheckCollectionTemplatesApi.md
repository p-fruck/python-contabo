# pfruck_contabo.CheckCollectionTemplatesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ext_check_collection_template**](CheckCollectionTemplatesApi.md#get_ext_check_collection_template) | **GET** /v1/troubleshooting/check-collection-templates/{checkCollectionTemplateId} | Get check
[**list_ext_check_collection_templates**](CheckCollectionTemplatesApi.md#list_ext_check_collection_templates) | **GET** /v1/troubleshooting/check-collection-templates | List check collection templates


# **get_ext_check_collection_template**
> ExtCheckCollectionTemplatesGetResponse get_ext_check_collection_template(x_request_id, check_collection_template_id, x_trace_id=x_trace_id)

Get check

Get a single check collection template by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_check_collection_templates_get_response import ExtCheckCollectionTemplatesGetResponse
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
    api_instance = pfruck_contabo.CheckCollectionTemplatesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    check_collection_template_id = 12345 # float | Check collection template's id
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get check
        api_response = api_instance.get_ext_check_collection_template(x_request_id, check_collection_template_id, x_trace_id=x_trace_id)
        print("The response of CheckCollectionTemplatesApi->get_ext_check_collection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckCollectionTemplatesApi->get_ext_check_collection_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **check_collection_template_id** | **float**| Check collection template&#39;s id | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ExtCheckCollectionTemplatesGetResponse**](ExtCheckCollectionTemplatesGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single check collection template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ext_check_collection_templates**
> ExtCheckCollectionTemplatesListResponse list_ext_check_collection_templates(x_request_id, x_trace_id=x_trace_id, object_type=object_type, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)

List check collection templates

List and filter all check collection templates

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.ext_check_collection_templates_list_response import ExtCheckCollectionTemplatesListResponse
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
    api_instance = pfruck_contabo.CheckCollectionTemplatesApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    object_type = 'vserver' # str | Object type for which the check template can be used (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    creation_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for created date (optional)
    creation_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for created date (optional)
    modification_start_time = '2021-06-03T06:27:12Z' # datetime | Start of search time range for modified date (optional)
    modification_end_time = '2021-06-03T10:27:12Z' # datetime | End of search time range for modified date (optional)

    try:
        # List check collection templates
        api_response = api_instance.list_ext_check_collection_templates(x_request_id, x_trace_id=x_trace_id, object_type=object_type, page=page, size=size, order_by=order_by, creation_start_time=creation_start_time, creation_end_time=creation_end_time, modification_start_time=modification_start_time, modification_end_time=modification_end_time)
        print("The response of CheckCollectionTemplatesApi->list_ext_check_collection_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckCollectionTemplatesApi->list_ext_check_collection_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **object_type** | **str**| Object type for which the check template can be used | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **creation_start_time** | **datetime**| Start of search time range for created date | [optional] 
 **creation_end_time** | **datetime**| End of search time range for created date | [optional] 
 **modification_start_time** | **datetime**| Start of search time range for modified date | [optional] 
 **modification_end_time** | **datetime**| End of search time range for modified date | [optional] 

### Return type

[**ExtCheckCollectionTemplatesListResponse**](ExtCheckCollectionTemplatesListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of check collection templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

