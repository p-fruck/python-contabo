# pfruck_contabo.UsersObjectStorageCredentialsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_object_storage_credentials**](UsersObjectStorageCredentialsApi.md#get_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/{objectStorageId}/credentials/{credentialId} | Get S3 compatible object storage credentials.
[**list_object_storage_credentials**](UsersObjectStorageCredentialsApi.md#list_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/credentials | Get list of S3 compatible object storage credentials for user.
[**regenerate_object_storage_credentials**](UsersObjectStorageCredentialsApi.md#regenerate_object_storage_credentials) | **PATCH** /v1/users/{userId}/object-storages/{objectStorageId}/credentials/{credentialId} | Regenerates secret key of specified user for the S3 compatible object storages.


# **get_object_storage_credentials**
> FindCredentialResponse get_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id, x_trace_id=x_trace_id)

Get S3 compatible object storage credentials.

Get S3 compatible object storage credentials for accessing it via S3 compatible tools like `aws` cli.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_credential_response import FindCredentialResponse
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
    api_instance = pfruck_contabo.UsersObjectStorageCredentialsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    object_storage_id = 'd8417276-d2d9-43a9-a0a8-9a6fa6060246' # str | The identifier of the S3 object storage
    credential_id = 12345 # int | The ID of the object storage credential
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get S3 compatible object storage credentials.
        api_response = api_instance.get_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id, x_trace_id=x_trace_id)
        print("The response of UsersObjectStorageCredentialsApi->get_object_storage_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersObjectStorageCredentialsApi->get_object_storage_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **object_storage_id** | **str**| The identifier of the S3 object storage | 
 **credential_id** | **int**| The ID of the object storage credential | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindCredentialResponse**](FindCredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains S3 credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object_storage_credentials**
> ListCredentialResponse list_object_storage_credentials(x_request_id, user_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, region_name=region_name, display_name=display_name)

Get list of S3 compatible object storage credentials for user.

Get list of S3 compatible object storage credentials for accessing it via S3 compatible tools like `aws` cli.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_credential_response import ListCredentialResponse
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
    api_instance = pfruck_contabo.UsersObjectStorageCredentialsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    object_storage_id = 'd8417276-d2d9-43a9-a0a8-9a6fa6060246' # str | The identifier of the S3 object storage (optional)
    region_name = 'Asia (Singapore)' # str | Filter for Object Storage by regions. Available regions: Asia (Singapore), European Union, United States (Central) (optional)
    display_name = 'Object Storage EU 420' # str | Filter for Object Storage by his displayName. (optional)

    try:
        # Get list of S3 compatible object storage credentials for user.
        api_response = api_instance.list_object_storage_credentials(x_request_id, user_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, object_storage_id=object_storage_id, region_name=region_name, display_name=display_name)
        print("The response of UsersObjectStorageCredentialsApi->list_object_storage_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersObjectStorageCredentialsApi->list_object_storage_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **object_storage_id** | **str**| The identifier of the S3 object storage | [optional] 
 **region_name** | **str**| Filter for Object Storage by regions. Available regions: Asia (Singapore), European Union, United States (Central) | [optional] 
 **display_name** | **str**| Filter for Object Storage by his displayName. | [optional] 

### Return type

[**ListCredentialResponse**](ListCredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be an array of JSON objects that contains S3 credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_object_storage_credentials**
> FindCredentialResponse regenerate_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id, x_trace_id=x_trace_id)

Regenerates secret key of specified user for the S3 compatible object storages.

Regenerates secret key of specified user for the a specific S3 compatible object storages.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.find_credential_response import FindCredentialResponse
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
    api_instance = pfruck_contabo.UsersObjectStorageCredentialsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    user_id = '6cdf5968-f9fe-4192-97c2-f349e813c5e8' # str | The identifier of the user.
    object_storage_id = 'd8417276-d2d9-43a9-a0a8-9a6fa6060246' # str | The identifier of the S3 object storage
    credential_id = 12345 # int | The ID of the object storage credential
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Regenerates secret key of specified user for the S3 compatible object storages.
        api_response = api_instance.regenerate_object_storage_credentials(x_request_id, user_id, object_storage_id, credential_id, x_trace_id=x_trace_id)
        print("The response of UsersObjectStorageCredentialsApi->regenerate_object_storage_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersObjectStorageCredentialsApi->regenerate_object_storage_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user. | 
 **object_storage_id** | **str**| The identifier of the S3 object storage | 
 **credential_id** | **int**| The ID of the object storage credential | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindCredentialResponse**](FindCredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains object storage S3 credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

