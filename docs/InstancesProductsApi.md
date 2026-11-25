# pfruck_contabo.InstancesProductsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_available_instance_products**](InstancesProductsApi.md#retrieve_available_instance_products) | **GET** /v1/compute/instances/{instanceId}/products/available | Get the available products of a specific instance


# **retrieve_available_instance_products**
> ListInstanceProductsResponse retrieve_available_instance_products(x_request_id, instance_id, x_trace_id=x_trace_id)

Get the available products of a specific instance

Get all products the instance can be upgraded to, excluding the currently assigned one. Use the `offerId` of the desired product to submit the upgrade.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.list_instance_products_response import ListInstanceProductsResponse
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
    api_instance = pfruck_contabo.InstancesProductsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    instance_id = 12345 # int | The identifier of the instance
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get the available products of a specific instance
        api_response = api_instance.retrieve_available_instance_products(x_request_id, instance_id, x_trace_id=x_trace_id)
        print("The response of InstancesProductsApi->retrieve_available_instance_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesProductsApi->retrieve_available_instance_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **instance_id** | **int**| The identifier of the instance | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**ListInstanceProductsResponse**](ListInstanceProductsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains the products available for the instance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

