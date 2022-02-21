# pfruck_contabo.ImagesApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_image**](ImagesApi.md#create_custom_image) | **POST** /v1/compute/images | Provide a custom image
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /v1/compute/images/{imageId} | Delete an uploaded custom image by its id
[**retrieve_custom_images_stats**](ImagesApi.md#retrieve_custom_images_stats) | **GET** /v1/compute/images/stats | List statistics regarding the customer&#39;s custom images
[**retrieve_image**](ImagesApi.md#retrieve_image) | **GET** /v1/compute/images/{imageId} | Get details about a specific image by its id
[**retrieve_image_list**](ImagesApi.md#retrieve_image_list) | **GET** /v1/compute/images | List available standard and custom images
[**update_image**](ImagesApi.md#update_image) | **PATCH** /v1/compute/images/{imageId} | Update custom image name by its id


# **create_custom_image**
> CreateCustomImageResponse create_custom_image(x_request_id, create_custom_image_request)

Provide a custom image

In order to provide a custom image please specify an URL from where the image can be directly downloaded. A custom image must be in either `.iso` or `.qcow2` format. Other formats will be rejected. Please note that downloading can take a while depending on network speed resp. bandwidth and size of image. You can check the status by retrieving information about the image via a GET request. Download will be rejected if you have exceeded your limits.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import images_api
from pfruck_contabo.model.create_custom_image_request import CreateCustomImageRequest
from pfruck_contabo.model.create_custom_image_response import CreateCustomImageResponse
from pfruck_contabo.model.create_custom_image_fail_response import CreateCustomImageFailResponse
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
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_custom_image_request = CreateCustomImageRequest(
        name="Ubuntu Custom Image",
        description="Ubuntu Server 20.04.2 LTS",
        url="https://example.com/image.qcow2",
        os_type="Linux",
        version="20.04.2",
    ) # CreateCustomImageRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Provide a custom image
        api_response = api_instance.create_custom_image(x_request_id, create_custom_image_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->create_custom_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Provide a custom image
        api_response = api_instance.create_custom_image(x_request_id, create_custom_image_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->create_custom_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **create_custom_image_request** | [**CreateCustomImageRequest**](CreateCustomImageRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CreateCustomImageResponse**](CreateCustomImageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard custom image attributes. |  -  |
**415** | The response will be an error in case the provided image URL is not in .qcow2 or .iso format.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> delete_image(x_request_id, image_id)

Delete an uploaded custom image by its id

Your are free to delete a previously uploaded custom images at any time.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import images_api
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
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    image_id = "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d" # str | The identifier of the image
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete an uploaded custom image by its id
        api_instance.delete_image(x_request_id, image_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an uploaded custom image by its id
        api_instance.delete_image(x_request_id, image_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **image_id** | **str**| The identifier of the image |
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

# **retrieve_custom_images_stats**
> CustomImagesStatsResponse retrieve_custom_images_stats(x_request_id)

List statistics regarding the customer's custom images

List statistics regarding the customer's custom images such as the number of custom images uploaded, used disk space, free available disk space and total available disk space

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import images_api
from pfruck_contabo.model.custom_images_stats_response import CustomImagesStatsResponse
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
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List statistics regarding the customer's custom images
        api_response = api_instance.retrieve_custom_images_stats(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->retrieve_custom_images_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List statistics regarding the customer's custom images
        api_response = api_instance.retrieve_custom_images_stats(x_request_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->retrieve_custom_images_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**CustomImagesStatsResponse**](CustomImagesStatsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the custom images count, the total available disk space, the used disk space and the free disk space. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_image**
> FindImageResponse retrieve_image(x_request_id, image_id)

Get details about a specific image by its id

Get details about a specific image. This could be either a standard or custom image. In case of an custom image you can also check the download status.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import images_api
from pfruck_contabo.model.find_image_response import FindImageResponse
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
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    image_id = "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d" # str | The identifier of the image
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details about a specific image by its id
        api_response = api_instance.retrieve_image(x_request_id, image_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->retrieve_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details about a specific image by its id
        api_response = api_instance.retrieve_image(x_request_id, image_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->retrieve_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **image_id** | **str**| The identifier of the image |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**FindImageResponse**](FindImageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard custom image attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_image_list**
> ListImageResponse retrieve_image_list(x_request_id)

List available standard and custom images

List and filter all available standard images provided by [Contabo](https://contabo.com) and your uploaded custom images.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import images_api
from pfruck_contabo.model.list_image_response import ListImageResponse
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
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    name = "Ubuntu" # str | The name of the image (optional)
    standard_image = True # bool | Flag indicating that image is either a standard (true) or a custom image (false) (optional)

    # example passing only required values which don't have defaults set
    try:
        # List available standard and custom images
        api_response = api_instance.retrieve_image_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->retrieve_image_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List available standard and custom images
        api_response = api_instance.retrieve_image_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, standard_image=standard_image)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->retrieve_image_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **name** | **str**| The name of the image | [optional]
 **standard_image** | **bool**| Flag indicating that image is either a standard (true) or a custom image (false) | [optional]

### Return type

[**ListImageResponse**](ListImageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains a paginated list of images. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> UpdateCustomImageResponse update_image(x_request_id, image_id, update_custom_image_request)

Update custom image name by its id

Update name of the custom image.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import images_api
from pfruck_contabo.model.update_custom_image_request import UpdateCustomImageRequest
from pfruck_contabo.model.update_custom_image_response import UpdateCustomImageResponse
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
    api_instance = images_api.ImagesApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    image_id = "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d" # str | The identifier of the image
    update_custom_image_request = UpdateCustomImageRequest(
        name="Ubuntu Custom Image",
        description="Ubuntu 20.04 image",
    ) # UpdateCustomImageRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update custom image name by its id
        api_response = api_instance.update_image(x_request_id, image_id, update_custom_image_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->update_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update custom image name by its id
        api_response = api_instance.update_image(x_request_id, image_id, update_custom_image_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling ImagesApi->update_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **image_id** | **str**| The identifier of the image |
 **update_custom_image_request** | [**UpdateCustomImageRequest**](UpdateCustomImageRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**UpdateCustomImageResponse**](UpdateCustomImageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard custom image attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

