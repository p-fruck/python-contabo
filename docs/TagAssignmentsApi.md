# pfruck_contabo.TagAssignmentsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assignment**](TagAssignmentsApi.md#create_assignment) | **POST** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Create a new assignment for the tag
[**delete_assignment**](TagAssignmentsApi.md#delete_assignment) | **DELETE** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Delete existing tag assignment
[**retrieve_assignment**](TagAssignmentsApi.md#retrieve_assignment) | **GET** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Get specific assignment for the tag
[**retrieve_assignment_list**](TagAssignmentsApi.md#retrieve_assignment_list) | **GET** /v1/tags/{tagId}/assignments | List tag assignments

# **create_assignment**
> CreateAssignmentResponse create_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)

Create a new assignment for the tag

Create a new tag assignment. This marks the specified resource with the specified tag for organizing purposes or to restrict access to that resource.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.TagAssignmentsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
tag_id = 789 # int | The identifier of the tag.
resource_type = 'resource_type_example' # str | The identifier of the resource type. Resource type is one of `instance|image`.
resource_id = 'resource_id_example' # str | The identifier of the resource id
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Create a new assignment for the tag
    api_response = api_instance.create_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assignment**
> delete_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)

Delete existing tag assignment

Tag assignment will be removed from the specified resource. If this tag is being used for access restrictions the affected users will no longer be able to access that resource.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.TagAssignmentsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
tag_id = 789 # int | The identifier of the tag.
resource_type = 'resource_type_example' # str | The identifier of the resource type. Resource type is one of `instance|image`.
resource_id = 'resource_id_example' # str | The identifier of the resource id
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete existing tag assignment
    api_instance.delete_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_assignment**
> FindAssignmentResponse retrieve_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)

Get specific assignment for the tag

Get attributes for a specific tag assignment in your account. For this the resource type and resource id is required.

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.TagAssignmentsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
tag_id = 789 # int | The identifier of the tag.
resource_type = 'resource_type_example' # str | The identifier of the resource type. Resource type is one of `instance|image`.
resource_id = 'resource_id_example' # str | The identifier of the resource id
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get specific assignment for the tag
    api_response = api_instance.retrieve_assignment(x_request_id, tag_id, resource_type, resource_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_assignment_list**
> ListAssignmentResponse retrieve_assignment_list(x_request_id, tag_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, resource_type=resource_type)

List tag assignments

List and filter all existing assignments for a tag in your account

### Example
```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.TagAssignmentsApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
tag_id = 789 # int | The identifier of the tag.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
resource_type = 'resource_type_example' # str | Filter as substring match for assignment resource type. Resource type is one of `instance|image`. (optional)

try:
    # List tag assignments
    api_response = api_instance.retrieve_assignment_list(x_request_id, tag_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
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
 **order_by** | [**list[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **resource_type** | **str**| Filter as substring match for assignment resource type. Resource type is one of &#x60;instance|image&#x60;. | [optional] 

### Return type

[**ListAssignmentResponse**](ListAssignmentResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

