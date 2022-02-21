# pfruck_contabo.TagAssignmentsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assignment**](TagAssignmentsApi.md#create_assignment) | **POST** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Create a new assignment for the tag
[**delete_assignment**](TagAssignmentsApi.md#delete_assignment) | **DELETE** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Delete existing tag assignment
[**retrieve_assignment**](TagAssignmentsApi.md#retrieve_assignment) | **GET** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Get specific assignment for the tag
[**retrieve_assignment_list**](TagAssignmentsApi.md#retrieve_assignment_list) | **GET** /v1/tags/{tagId}/assignments | List tag assignments


# **create_assignment**
> CreateAssignmentResponse create_assignment(x_request_id, tag_id, resource_type, resource_id)

Create a new assignment for the tag

Create a new tag assignment. This marks the specified resource with the specified tag for organizing purposes or to restrict access to that resource.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import tag_assignments_api
from pfruck_contabo.model.create_assignment_response import CreateAssignmentResponse
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
    api_instance = tag_assignments_api.TagAssignmentsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    tag_id = 12345 # int | The identifier of the tag.
    resource_type = "instance" # str | The identifier of the resource type. Resource type is one of `instance|image`.
    resource_id = "d65ecf3b-30db-4dc2-9e88-dfc21a14a6bc" # str | The identifier of the resource id
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new assignment for the tag
        api_response = api_instance.create_assignment(x_request_id, tag_id, resource_type, resource_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->create_assignment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new assignment for the tag
        api_response = api_instance.create_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->create_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **tag_id** | **int**| The identifier of the tag. |
 **resource_type** | **str**| The identifier of the resource type. Resource type is one of &#x60;instance|image&#x60;. |
 **resource_id** | **str**| The identifier of the resource id |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CreateAssignmentResponse**](CreateAssignmentResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard tag assignment attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assignment**
> delete_assignment(x_request_id, tag_id, resource_type, resource_id)

Delete existing tag assignment

Tag assignment will be removed from the specified resource. If this tag is being used for access restrictions the affected users will no longer be able to access that resource.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import tag_assignments_api
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
    api_instance = tag_assignments_api.TagAssignmentsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    tag_id = 12345 # int | The identifier of the tag.
    resource_type = "instance" # str | The identifier of the resource type. Resource type is one of `instance|image`.
    resource_id = "d65ecf3b-30db-4dc2-9e88-dfc21a14a6bc" # str | The identifier of the resource id
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete existing tag assignment
        api_instance.delete_assignment(x_request_id, tag_id, resource_type, resource_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->delete_assignment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete existing tag assignment
        api_instance.delete_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->delete_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **tag_id** | **int**| The identifier of the tag. |
 **resource_type** | **str**| The identifier of the resource type. Resource type is one of &#x60;instance|image&#x60;. |
 **resource_id** | **str**| The identifier of the resource id |
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

# **retrieve_assignment**
> FindAssignmentResponse retrieve_assignment(x_request_id, tag_id, resource_type, resource_id)

Get specific assignment for the tag

Get attributes for a specific tag assignment in your account. For this the resource type and resource id is required.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import tag_assignments_api
from pfruck_contabo.model.find_assignment_response import FindAssignmentResponse
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
    api_instance = tag_assignments_api.TagAssignmentsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    tag_id = 12345 # int | The identifier of the tag.
    resource_type = "instance" # str | The identifier of the resource type. Resource type is one of `instance|image`.
    resource_id = "d65ecf3b-30db-4dc2-9e88-dfc21a14a6bc" # str | The identifier of the resource id
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific assignment for the tag
        api_response = api_instance.retrieve_assignment(x_request_id, tag_id, resource_type, resource_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->retrieve_assignment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific assignment for the tag
        api_response = api_instance.retrieve_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->retrieve_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **tag_id** | **int**| The identifier of the tag. |
 **resource_type** | **str**| The identifier of the resource type. Resource type is one of &#x60;instance|image&#x60;. |
 **resource_id** | **str**| The identifier of the resource id |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindAssignmentResponse**](FindAssignmentResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard tag assignment attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_assignment_list**
> ListAssignmentResponse retrieve_assignment_list(x_request_id, tag_id)

List tag assignments

List and filter all existing assignments for a tag in your account

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import tag_assignments_api
from pfruck_contabo.model.list_assignment_response import ListAssignmentResponse
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
    api_instance = tag_assignments_api.TagAssignmentsApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    tag_id = 12345 # int | The identifier of the tag.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    resource_type = "instance" # str | Filter as substring match for assignment resource type. Resource type is one of `instance|image`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List tag assignments
        api_response = api_instance.retrieve_assignment_list(x_request_id, tag_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->retrieve_assignment_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List tag assignments
        api_response = api_instance.retrieve_assignment_list(x_request_id, tag_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, resource_type=resource_type)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling TagAssignmentsApi->retrieve_assignment_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **tag_id** | **int**| The identifier of the tag. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **resource_type** | **str**| Filter as substring match for assignment resource type. Resource type is one of &#x60;instance|image&#x60;. | [optional]

### Return type

[**ListAssignmentResponse**](ListAssignmentResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of tag assignments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

