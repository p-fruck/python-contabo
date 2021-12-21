# pfruck_contabo.RolesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /v1/roles/{roleType} | Create a new role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleType}/{roleId} | Delete existing role by id
[**retrieve_api_permissions_list**](RolesApi.md#retrieve_api_permissions_list) | **GET** /v1/roles/api-permissions | List of API permissions
[**retrieve_role**](RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleType}/{roleId} | Get specific role by id
[**retrieve_role_list**](RolesApi.md#retrieve_role_list) | **GET** /v1/roles/{roleType} | List roles
[**update_role**](RolesApi.md#update_role) | **PATCH** /v1/roles/{roleType}/{roleId} | Update specific role by id

# **create_role**
> CreateRoleResponse create_role(body, x_request_id, role_type, x_trace_id=x_trace_id)

Create a new role

Create a new role. Roles can have two types `apiPermission` (restricting access to api endpoints) and `resourcePermission` (restricting access to resources like compute). In order to get a list availbale api enpoints please refer to the GET api-permissions endpoint. For specifying a role of type `resourcePermission` please use tag ids. For those to take effect please assign them to a resource in the tag management api.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.RolesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateRoleRequest() # CreateRoleRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
role_type = 'role_type_example' # str | Role type can be either `resourcePermission` for accessing specific resources or `apiPermission` for accessing specific API endpoints.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new role
    api_response = api_instance.create_role(body, x_request_id, role_type, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleRequest**](CreateRoleRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **role_type** | **str**| Role type can be either &#x60;resourcePermission&#x60; for accessing specific resources or &#x60;apiPermission&#x60; for accessing specific API endpoints. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**CreateRoleResponse**](CreateRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(x_request_id, role_type, role_id, x_trace_id=x_trace_id)

Delete existing role by id

You can't delete a role if it is still assigned to a user. In such cases please remove the role from the users.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.RolesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
role_type = 'role_type_example' # str | Role type can be either `resourcePermission` for accessing specific resources or `apiPermission` for accessing specific API endpoints.
role_id = 789 # int | The identifier of the role
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete existing role by id
    api_instance.delete_role(x_request_id, role_type, role_id, x_trace_id=x_trace_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **role_type** | **str**| Role type can be either &#x60;resourcePermission&#x60; for accessing specific resources or &#x60;apiPermission&#x60; for accessing specific API endpoints. | 
 **role_id** | **int**| The identifier of the role | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_api_permissions_list**
> ListApiPermissionResponse retrieve_api_permissions_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, api_name=api_name)

List of API permissions

List all available API permissions. This list serves as a reference for specifying roles of type `apiPermission`. As endpoints differ in their possibilities not all actions are available for each endpoint.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.RolesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
api_name = 'api_name_example' # str | The name of api (optional)

try:
    # List of API permissions
    api_response = api_instance.retrieve_api_permissions_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, api_name=api_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->retrieve_api_permissions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **api_name** | **str**| The name of api | [optional] 

### Return type

[**ListApiPermissionResponse**](ListApiPermissionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_role**
> FindRoleResponse retrieve_role(x_request_id, role_type, role_id, x_trace_id=x_trace_id)

Get specific role by id

Get attributes of specific role.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.RolesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
role_type = 'role_type_example' # str | Role type can be either `resourcePermission` for accessing specific resources or `apiPermission` for accessing specific API endpoints.
role_id = 789 # int | The identifier of the role
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get specific role by id
    api_response = api_instance.retrieve_role(x_request_id, role_type, role_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->retrieve_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **role_type** | **str**| Role type can be either &#x60;resourcePermission&#x60; for accessing specific resources or &#x60;apiPermission&#x60; for accessing specific API endpoints. | 
 **role_id** | **int**| The identifier of the role | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**FindRoleResponse**](FindRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_role_list**
> ListRoleResponse retrieve_role_list(x_request_id, role_type, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, api_name=api_name, tag_name=tag_name)

List roles

List and filter all your roles. A role allows you to specify permission to api endpoints and resources like compute.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.RolesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
role_type = 'role_type_example' # str | Role type can be either `resourcePermission` for accessing specific resources or `apiPermission` for accessing specific API endpoints.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
name = 'name_example' # str | The name of the role (optional)
api_name = 'api_name_example' # str | The name of api (optional)
tag_name = 'tag_name_example' # str | The name of the tag (optional)

try:
    # List roles
    api_response = api_instance.retrieve_role_list(x_request_id, role_type, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, api_name=api_name, tag_name=tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->retrieve_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **role_type** | **str**| Role type can be either &#x60;resourcePermission&#x60; for accessing specific resources or &#x60;apiPermission&#x60; for accessing specific API endpoints. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **name** | **str**| The name of the role | [optional] 
 **api_name** | **str**| The name of api | [optional] 
 **tag_name** | **str**| The name of the tag | [optional] 

### Return type

[**ListRoleResponse**](ListRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> UpdateRoleResponse update_role(body, x_request_id, role_type, role_id, x_trace_id=x_trace_id)

Update specific role by id

Update attributes to your role. Attributes are optional. If not set, the attributes will retain their original values.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.RolesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpdateRoleRequest() # UpdateRoleRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
role_type = 'role_type_example' # str | Role type can be either `resourcePermission` for accessing specific resources or `apiPermission` for accessing specific API endpoints.
role_id = 789 # int | The identifier of the role
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Update specific role by id
    api_response = api_instance.update_role(body, x_request_id, role_type, role_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRoleRequest**](UpdateRoleRequest.md)|  | 
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **role_type** | **str**| Role type can be either &#x60;resourcePermission&#x60; for accessing specific resources or &#x60;apiPermission&#x60; for accessing specific API endpoints. | 
 **role_id** | **int**| The identifier of the role | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**UpdateRoleResponse**](UpdateRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

