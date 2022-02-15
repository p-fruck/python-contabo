# pfruck_contabo.SecretsApi

All URIs are relative to *https://api.contabo.intra*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret**](SecretsApi.md#create_secret) | **POST** /v1/secrets | Create a new secret
[**delete_secret**](SecretsApi.md#delete_secret) | **DELETE** /v1/secrets/{secretId} | Delete existing secret by id
[**retrieve_secret**](SecretsApi.md#retrieve_secret) | **GET** /v1/secrets/{secretId} | Get specific secret by id
[**retrieve_secret_list**](SecretsApi.md#retrieve_secret_list) | **GET** /v1/secrets | List secrets
[**update_secret**](SecretsApi.md#update_secret) | **PATCH** /v1/secrets/{secretId} | Update specific secret by id

# **create_secret**
> CreateSecretResponse create_secret(body, x_request_id, x_trace_id=x_trace_id)

Create a new secret

Create a new secret in your account with attributes name, type and value. Attribute type can be password or ssh.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SecretsApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateSecretRequest() # CreateSecretRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new secret
    api_response = api_instance.create_secret(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->create_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSecretRequest**](CreateSecretRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateSecretResponse**](CreateSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret**
> delete_secret(x_request_id, secret_id, x_trace_id=x_trace_id)

Delete existing secret by id

You can remove a specific secret from your account

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SecretsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
secret_id = 789 # int | The id of the secret
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete existing secret by id
    api_instance.delete_secret(x_request_id, secret_id, x_trace_id=x_trace_id)
except ApiException as e:
    print("Exception when calling SecretsApi->delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **secret_id** | **int**| The id of the secret | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_secret**
> FindSecretResponse retrieve_secret(x_request_id, secret_id, x_trace_id=x_trace_id)

Get specific secret by id

Get attributes values for a specific secret on your account.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SecretsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
secret_id = 789 # int | The id of the secret
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get specific secret by id
    api_response = api_instance.retrieve_secret(x_request_id, secret_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->retrieve_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **secret_id** | **int**| The id of the secret | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindSecretResponse**](FindSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_secret_list**
> ListSecretResponse retrieve_secret_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, type=type)

List secrets

List and filter all secrets in your account.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SecretsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
name = 'name_example' # str | Filter secrets by name (optional)
type = 'type_example' # str | Filter secrets by type (optional)

try:
    # List secrets
    api_response = api_instance.retrieve_secret_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->retrieve_secret_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| Filter secrets by name | [optional] 
 **type** | **str**| Filter secrets by type | [optional] 

### Return type

[**ListSecretResponse**](ListSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret**
> UpdateSecretResponse update_secret(body, x_request_id, secret_id, x_trace_id=x_trace_id)

Update specific secret by id

Update attributes to your secret. Attributes are optional. If not set, the attributes will retain their original values. Only name and value can be updated.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.SecretsApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpdateSecretRequest() # UpdateSecretRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
secret_id = 789 # int | The id of the secret
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Update specific secret by id
    api_response = api_instance.update_secret(body, x_request_id, secret_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->update_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSecretRequest**](UpdateSecretRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **secret_id** | **int**| The id of the secret | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpdateSecretResponse**](UpdateSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

