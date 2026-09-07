# pfruck_contabo.DomainsApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_domain**](DomainsApi.md#cancel_domain) | **POST** /v1/domains/{domain}/cancel | Cancel a specific domain
[**confirm_domain_transfer_out**](DomainsApi.md#confirm_domain_transfer_out) | **POST** /v1/domains/{domain}/transfer-out | Confirm transfer out for a domain
[**confirm_domain_transfer_out_0**](DomainsApi.md#confirm_domain_transfer_out_0) | **POST** /v1/domains/{domain}/transfer-out | Confirm transfer out for a domain
[**get_auth_code**](DomainsApi.md#get_auth_code) | **POST** /v1/domains/{domain}/generate-auth-code | Get auth code for a domain
[**list_domains**](DomainsApi.md#list_domains) | **GET** /v1/domains | List all domains
[**list_pending_actions**](DomainsApi.md#list_pending_actions) | **GET** /v1/domains/pending-actions | List pending domain actions
[**order_domain**](DomainsApi.md#order_domain) | **POST** /v1/domains | Create or transfer a domain
[**retrieve_domain**](DomainsApi.md#retrieve_domain) | **GET** /v1/domains/{domain} | List specific domain
[**revoke_cancel_domain**](DomainsApi.md#revoke_cancel_domain) | **POST** /v1/domains/{domain}/revoke-cancellation | Revoke cancellation for a specific domain
[**revoke_domain_transfer_out**](DomainsApi.md#revoke_domain_transfer_out) | **DELETE** /v1/domains/{domain}/transfer-out | Revoke transfer out for a domain
[**revoke_domain_transfer_out_0**](DomainsApi.md#revoke_domain_transfer_out_0) | **DELETE** /v1/domains/{domain}/transfer-out | Revoke transfer out for a domain
[**update_domain**](DomainsApi.md#update_domain) | **PATCH** /v1/domains/{domain} | Update a specific domain
[**validate_domain_availability**](DomainsApi.md#validate_domain_availability) | **POST** /v1/registries-domains/{domain}/check-availability | Check domain availablility


# **cancel_domain**
> DomainCancelResponse cancel_domain(x_request_id, domain, cancel_domain_request, x_trace_id=x_trace_id)

Cancel a specific domain

Cancel a specific domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.cancel_domain_request import CancelDomainRequest
from pfruck_contabo.models.domain_cancel_response import DomainCancelResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    cancel_domain_request = pfruck_contabo.CancelDomainRequest() # CancelDomainRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Cancel a specific domain
        api_response = api_instance.cancel_domain(x_request_id, domain, cancel_domain_request, x_trace_id=x_trace_id)
        print("The response of DomainsApi->cancel_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->cancel_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
 **cancel_domain_request** | [**CancelDomainRequest**](CancelDomainRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**DomainCancelResponse**](DomainCancelResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response body has no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_domain_transfer_out**
> confirm_domain_transfer_out(x_request_id, domain, x_trace_id=x_trace_id)

Confirm transfer out for a domain

Confirm transfer out for a domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Confirm transfer out for a domain
        api_instance.confirm_domain_transfer_out(x_request_id, domain, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DomainsApi->confirm_domain_transfer_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
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

# **confirm_domain_transfer_out_0**
> confirm_domain_transfer_out_0(x_request_id, domain, x_trace_id=x_trace_id)

Confirm transfer out for a domain

Confirm transfer out for a domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Confirm transfer out for a domain
        api_instance.confirm_domain_transfer_out_0(x_request_id, domain, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DomainsApi->confirm_domain_transfer_out_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
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

# **get_auth_code**
> DomainAuthCodeRegenerateResponse get_auth_code(x_request_id, domain, x_trace_id=x_trace_id)

Get auth code for a domain

Get auth code for a domain by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.domain_auth_code_regenerate_response import DomainAuthCodeRegenerateResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Get auth code for a domain
        api_response = api_instance.get_auth_code(x_request_id, domain, x_trace_id=x_trace_id)
        print("The response of DomainsApi->get_auth_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_auth_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**DomainAuthCodeRegenerateResponse**](DomainAuthCodeRegenerateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains auth code of domain requested |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> DomainsListResponse list_domains(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, sld=sld, tld=tld, status=status)

List all domains

List and filter all your domains

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.domains_list_response import DomainsListResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = ['name:asc'] # List[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    sld = 'testDomain' # str | Filter as substring match for domain sld. (optional)
    tld = 'de' # str | Filter as substring match for domain tld. (optional)
    status = 'ready' # str | Filter domains by status (optional)

    try:
        # List all domains
        api_response = api_instance.list_domains(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, sld=sld, tld=tld, status=status)
        print("The response of DomainsApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 
 **page** | **int**| Number of page to be fetched. | [optional] 
 **size** | **int**| Number of elements per page. | [optional] 
 **order_by** | [**List[str]**](str.md)| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional] 
 **sld** | **str**| Filter as substring match for domain sld. | [optional] 
 **tld** | **str**| Filter as substring match for domain tld. | [optional] 
 **status** | **str**| Filter domains by status | [optional] 

### Return type

[**DomainsListResponse**](DomainsListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard domains attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pending_actions**
> DomainPendingActionsListResponse list_pending_actions(x_request_id, x_trace_id=x_trace_id)

List pending domain actions

List the calling customer's domains with an unacknowledged outbound transfer (ACK/NACK) pending. Live OpusDNS read for OpusDNS-routed customers; empty payload (no upstream call) for everyone else.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.domain_pending_actions_list_response import DomainPendingActionsListResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # List pending domain actions
        api_response = api_instance.list_pending_actions(x_request_id, x_trace_id=x_trace_id)
        print("The response of DomainsApi->list_pending_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_pending_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**DomainPendingActionsListResponse**](DomainPendingActionsListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object with &#x60;data&#x60; (domains pending an outbound-transfer ACK/NACK) and &#x60;_links&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_domain**
> DomainCreateResponse order_domain(x_request_id, domain_create_request, x_trace_id=x_trace_id)

Create or transfer a domain

Create or transfer a domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.domain_create_request import DomainCreateRequest
from pfruck_contabo.models.domain_create_response import DomainCreateResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain_create_request = pfruck_contabo.DomainCreateRequest() # DomainCreateRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Create or transfer a domain
        api_response = api_instance.order_domain(x_request_id, domain_create_request, x_trace_id=x_trace_id)
        print("The response of DomainsApi->order_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->order_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain_create_request** | [**DomainCreateRequest**](DomainCreateRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**DomainCreateResponse**](DomainCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard domain attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_domain**
> DomainFindResponse retrieve_domain(x_request_id, domain, x_trace_id=x_trace_id)

List specific domain

List specific domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.domain_find_response import DomainFindResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # List specific domain
        api_response = api_instance.retrieve_domain(x_request_id, domain, x_trace_id=x_trace_id)
        print("The response of DomainsApi->retrieve_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->retrieve_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**DomainFindResponse**](DomainFindResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard domains attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_cancel_domain**
> revoke_cancel_domain(x_request_id, domain, x_trace_id=x_trace_id)

Revoke cancellation for a specific domain

Revoke cancellation for a specific domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Revoke cancellation for a specific domain
        api_instance.revoke_cancel_domain(x_request_id, domain, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DomainsApi->revoke_cancel_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
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

# **revoke_domain_transfer_out**
> revoke_domain_transfer_out(x_request_id, domain, x_trace_id=x_trace_id)

Revoke transfer out for a domain

Revoke transfer out for a domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Revoke transfer out for a domain
        api_instance.revoke_domain_transfer_out(x_request_id, domain, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DomainsApi->revoke_domain_transfer_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
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

# **revoke_domain_transfer_out_0**
> revoke_domain_transfer_out_0(x_request_id, domain, x_trace_id=x_trace_id)

Revoke transfer out for a domain

Revoke transfer out for a domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Revoke transfer out for a domain
        api_instance.revoke_domain_transfer_out_0(x_request_id, domain, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DomainsApi->revoke_domain_transfer_out_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
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

# **update_domain**
> DomainPatchResponse update_domain(x_request_id, domain, domain_patch_request, x_trace_id=x_trace_id)

Update a specific domain

Update nameservers and handles for a specific domain

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
from pfruck_contabo.models.domain_patch_request import DomainPatchRequest
from pfruck_contabo.models.domain_patch_response import DomainPatchResponse
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    domain_patch_request = pfruck_contabo.DomainPatchRequest() # DomainPatchRequest | 
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Update a specific domain
        api_response = api_instance.update_domain(x_request_id, domain, domain_patch_request, x_trace_id=x_trace_id)
        print("The response of DomainsApi->update_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
 **domain_patch_request** | [**DomainPatchRequest**](DomainPatchRequest.md)|  | 
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional] 

### Return type

[**DomainPatchResponse**](DomainPatchResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard domains attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_domain_availability**
> validate_domain_availability(x_request_id, domain, x_trace_id=x_trace_id)

Check domain availablility

Check if a specific domain is available or not

### Example

* Bearer (JWT) Authentication (bearer):

```python
import pfruck_contabo
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
    api_instance = pfruck_contabo.DomainsApi(api_client)
    x_request_id = '04e0f898-37b4-48bc-a794-1a57abe6aa31' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    domain = 'testDomain.de' # str | Domain Name
    x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

    try:
        # Check domain availablility
        api_instance.validate_domain_availability(x_request_id, domain, x_trace_id=x_trace_id)
    except Exception as e:
        print("Exception when calling DomainsApi->validate_domain_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. | 
 **domain** | **str**| Domain Name | 
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
**204** | The response signifies that the domain is available |  -  |
**404** | The response signifies that the domain is not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

