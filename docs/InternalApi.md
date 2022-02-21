# pfruck_contabo.InternalApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket**](InternalApi.md#create_ticket) | **POST** /v1/create-ticket | Create a new support ticket
[**get_object_storage_credentials**](InternalApi.md#get_object_storage_credentials) | **GET** /v1/users/{userId}/object-storages/credentials | Get S3 compatible object storage credentials
[**regenerate_credentials**](InternalApi.md#regenerate_credentials) | **PATCH** /v1/users/{userId}/object-storages/credentials | Regenerates secret key of specified user for the S3 compatible object storages
[**retrieve_user_is_password_set**](InternalApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status

# **create_ticket**
> CreateTicketResponse create_ticket(body, x_request_id, x_trace_id=x_trace_id)

Create a new support ticket

Create a new support ticket.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InternalApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateTicketRequest() # CreateTicketRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new support ticket
    api_response = api_instance.create_ticket(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->create_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTicketRequest**](CreateTicketRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateTicketResponse**](CreateTicketResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_credentials**
> CredentialResponse get_object_storage_credentials(x_request_id, user_id, x_trace_id=x_trace_id)

Get S3 compatible object storage credentials

Get S3 compatible object storage credentials for accessing it via S3 compatible tools like `aws` cli.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InternalApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get S3 compatible object storage credentials
    api_response = api_instance.get_object_storage_credentials(x_request_id, user_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->get_object_storage_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_credentials**
> CredentialResponse regenerate_credentials(x_request_id, user_id, x_trace_id=x_trace_id)

Regenerates secret key of specified user for the S3 compatible object storages

Regenerates secret key of specified user for the S3 compatible object storages. Please note that these credentials are valid for all object storages at different locations.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InternalApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Regenerates secret key of specified user for the S3 compatible object storages
    api_response = api_instance.regenerate_credentials(x_request_id, user_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->regenerate_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CredentialResponse**](CredentialResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_is_password_set**
> FindUserIsPasswordSetResponse retrieve_user_is_password_set(x_request_id, x_trace_id=x_trace_id, user_id=user_id)

Get user is password set status

Get info about idm user if the password is set.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.InternalApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
user_id = 'user_id_example' # str | The user ID for checking if password is set for him (optional)

try:
    # Get user is password set status
    api_response = api_instance.retrieve_user_is_password_set(x_request_id, x_trace_id=x_trace_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->retrieve_user_is_password_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **user_id** | **str**| The user ID for checking if password is set for him | [optional] 

### Return type

[**FindUserIsPasswordSetResponse**](FindUserIsPasswordSetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

