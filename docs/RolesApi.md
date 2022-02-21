# pfruck_contabo.RolesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /v1/roles | Create a new role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Delete existing role by id
[**retrieve_api_permissions_list**](RolesApi.md#retrieve_api_permissions_list) | **GET** /v1/roles/api-permissions | List of API permissions
[**retrieve_role**](RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleId} | Get specific role by id
[**retrieve_role_list**](RolesApi.md#retrieve_role_list) | **GET** /v1/roles | List roles
[**update_role**](RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update specific role by id


# **create_role**
> CreateRoleResponse create_role(x_request_id, create_role_request)

Create a new role

Create a new role. In order to get a list availbale api enpoints (apiName) and their actions please refer to the GET api-permissions endpoint. For specifying `resources` please enter tag ids. For those to take effect please assign them to a resource in the tag management api.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import roles_api
from pfruck_contabo.model.create_role_response import CreateRoleResponse
from pfruck_contabo.model.create_role_request import CreateRoleRequest
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
    api_instance = roles_api.RolesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_role_request = CreateRoleRequest(
        name="infrastructure",
        admin=False,
        access_all_resources=False,
        permissions=[
            PermissionRequest(
                api_name="infrastructure",
                actions=["CREATE","READ"],
                resources=[1,2,3],
            ),
        ],
    ) # CreateRoleRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new role
        api_response = api_instance.create_role(x_request_id, create_role_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new role
        api_response = api_instance.create_role(x_request_id, create_role_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CreateRoleResponse**](CreateRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard role attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(x_request_id, role_id)

Delete existing role by id

You can't delete a role if it is still assigned to a user. In such cases please remove the role from the users.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    role_id = 12345 # int | The identifier of the role
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete existing role by id
        api_instance.delete_role(x_request_id, role_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete existing role by id
        api_instance.delete_role(x_request_id, role_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **role_id** | **int**| The identifier of the role |
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

# **retrieve_api_permissions_list**
> ListApiPermissionResponse retrieve_api_permissions_list(x_request_id)

List of API permissions

List all available API permissions. This list serves as a reference for specifying roles. As endpoints differ in their possibilities not all actions are available for each endpoint.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import roles_api
from pfruck_contabo.model.list_api_permission_response import ListApiPermissionResponse
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
    api_instance = roles_api.RolesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    api_name = "/v1/compute/instances" # str | The name of api (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of API permissions
        api_response = api_instance.retrieve_api_permissions_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->retrieve_api_permissions_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of API permissions
        api_response = api_instance.retrieve_api_permissions_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, api_name=api_name)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->retrieve_api_permissions_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **api_name** | **str**| The name of api | [optional]

### Return type

[**ListApiPermissionResponse**](ListApiPermissionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of API permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_role**
> FindRoleResponse retrieve_role(x_request_id, role_id)

Get specific role by id

Get attributes of specific role.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import roles_api
from pfruck_contabo.model.find_role_response import FindRoleResponse
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
    api_instance = roles_api.RolesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    role_id = 12345 # int | The identifier of the role
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific role by id
        api_response = api_instance.retrieve_role(x_request_id, role_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->retrieve_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific role by id
        api_response = api_instance.retrieve_role(x_request_id, role_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->retrieve_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **role_id** | **int**| The identifier of the role |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindRoleResponse**](FindRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard role attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_role_list**
> ListRoleResponse retrieve_role_list(x_request_id)

List roles

List and filter all your roles. A role allows you to specify permission to api endpoints and resources like compute.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import roles_api
from pfruck_contabo.model.list_role_response import ListRoleResponse
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
    api_instance = roles_api.RolesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = "Web" # str | The name of the role (optional)
    api_name = "/v1/compute/instances" # str | The name of api (optional)
    tag_name = "Web" # str | The name of the tag (optional)
    type = "custom" # str | The type of the tag. Can be either `default` or `custom` (optional)

    # example passing only required values which don't have defaults set
    try:
        # List roles
        api_response = api_instance.retrieve_role_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->retrieve_role_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List roles
        api_response = api_instance.retrieve_role_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, api_name=api_name, tag_name=tag_name, type=type)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->retrieve_role_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **name** | **str**| The name of the role | [optional]
 **api_name** | **str**| The name of api | [optional]
 **tag_name** | **str**| The name of the tag | [optional]
 **type** | **str**| The type of the tag. Can be either &#x60;default&#x60; or &#x60;custom&#x60; | [optional]

### Return type

[**ListRoleResponse**](ListRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> UpdateRoleResponse update_role(x_request_id, role_id, update_role_request)

Update specific role by id

Update attributes to your role. Attributes are optional. If not set, the attributes will retain their original values.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import roles_api
from pfruck_contabo.model.update_role_request import UpdateRoleRequest
from pfruck_contabo.model.update_role_response import UpdateRoleResponse
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
    api_instance = roles_api.RolesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    role_id = 12345 # int | The identifier of the role
    update_role_request = UpdateRoleRequest(
        name="infrastructure",
        admin=False,
        access_all_resources=False,
        permissions=[
            PermissionRequest(
                api_name="infrastructure",
                actions=["CREATE","READ"],
                resources=[1,2,3],
            ),
        ],
    ) # UpdateRoleRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update specific role by id
        api_response = api_instance.update_role(x_request_id, role_id, update_role_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update specific role by id
        api_response = api_instance.update_role(x_request_id, role_id, update_role_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **role_id** | **int**| The identifier of the role |
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**UpdateRoleResponse**](UpdateRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard role attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

