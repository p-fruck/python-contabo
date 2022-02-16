# pfruck_contabo.UsersApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v1/users | Create a new user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete existing user by id
[**generate_client_secret**](UsersApi.md#generate_client_secret) | **PUT** /v1/users/client/secret | Generate new client secret
[**resend_email_verification**](UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
[**reset_password**](UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
[**retrieve_user**](UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
[**retrieve_user_client**](UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
[**retrieve_user_list**](UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
[**update_user**](UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id

# **create_user**
> CreateUserResponse create_user(body, x_request_id, x_trace_id=x_trace_id)

Create a new user

Create a new user with required attributes name, email, enabled, totp (=Two-factor authentication 2FA), admin (=access to all endpoints and resources), accessAllResources and roles. You can't specify any password / secrets for the user. For security reasons the user will have to specify secrets on his own.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateUserRequest() # CreateUserRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new user
    api_response = api_instance.create_user(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(x_request_id, user_id, x_trace_id=x_trace_id)

Delete existing user by id

By deleting a user he will not be able to access any endpoints or resources any longer. In order to temporarily disable a user please update its `enabled` attribute.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete existing user by id
    api_instance.delete_user(x_request_id, user_id, x_trace_id=x_trace_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_client_secret**
> GenerateClientSecretResponse generate_client_secret(x_request_id, x_trace_id=x_trace_id)

Generate new client secret

Generate and get new client secret.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Generate new client secret
    api_response = api_instance.generate_client_secret(x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->generate_client_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**GenerateClientSecretResponse**](GenerateClientSecretResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_verification**
> resend_email_verification(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)

Resend email verification

Resend email verification for a specific user

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
redirect_url = 'redirect_url_example' # str | The redirect url used for email verification (optional)

try:
    # Resend email verification
    api_instance.resend_email_verification(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)
except ApiException as e:
    print("Exception when calling UsersApi->resend_email_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **redirect_url** | **str**| The redirect url used for email verification | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)

Send reset password email

Send reset password email for a specific user

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
redirect_url = 'redirect_url_example' # str | The redirect url used for resetting password (optional)

try:
    # Send reset password email
    api_instance.reset_password(x_request_id, user_id, x_trace_id=x_trace_id, redirect_url=redirect_url)
except ApiException as e:
    print("Exception when calling UsersApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **redirect_url** | **str**| The redirect url used for resetting password | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user**
> FindUserResponse retrieve_user(x_request_id, user_id, x_trace_id=x_trace_id)

Get specific user by id

Get attributes for a specific user.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get specific user by id
    api_response = api_instance.retrieve_user(x_request_id, user_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindUserResponse**](FindUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_client**
> FindClientResponse retrieve_user_client(x_request_id, x_trace_id=x_trace_id)

Get client

Get idm client.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get client
    api_response = api_instance.retrieve_user_client(x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_user_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindClientResponse**](FindClientResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user_list**
> ListUserResponse retrieve_user_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, enabled=enabled, owner=owner)

List users

List and filter all your users.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
email = 'email_example' # str | Filter as substring match for user emails. (optional)
enabled = true # bool | Filter if user is enabled or not. (optional)
owner = true # bool | Filter if user is owner or not. (optional)

try:
    # List users
    api_response = api_instance.retrieve_user_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, email=email, enabled=enabled, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **email** | **str**| Filter as substring match for user emails. | [optional] 
 **enabled** | **bool**| Filter if user is enabled or not. | [optional] 
 **owner** | **bool**| Filter if user is owner or not. | [optional] 

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UpdateUserResponse update_user(body, x_request_id, user_id, x_trace_id=x_trace_id)

Update specific user by id

Update attributes of a user. You may only specify the attributes you want to change. If an attribute is not set, it will retain its original value.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.UsersApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpdateUserRequest() # UpdateUserRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
user_id = 'user_id_example' # str | The identifier of the user
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Update specific user by id
    api_response = api_instance.update_user(body, x_request_id, user_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **user_id** | **str**| The identifier of the user | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

