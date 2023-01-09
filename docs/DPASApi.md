# pfruck_contabo.DPASApi

All URIs are relative to *https://api.contabo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conclude_dpa**](DPASApi.md#conclude_dpa) | **POST** /v1/dpas/{dpaId}/conclude | Concludes a data processing agreement
[**create_dpa**](DPASApi.md#create_dpa) | **POST** /v1/dpas | Create a new data processing agreement
[**download_dpa_file**](DPASApi.md#download_dpa_file) | **GET** /v1/dpas/{dpaId}/download | Download concluded DPA PDF file
[**download_preview_dpa**](DPASApi.md#download_preview_dpa) | **GET** /v1/dpas/{dpaId}/preview | Download preview version of DPA
[**list_dpa_services**](DPASApi.md#list_dpa_services) | **GET** /v1/dpas/services | List services
[**retrieve_dpa**](DPASApi.md#retrieve_dpa) | **GET** /v1/dpas/{dpaId} | Get specific Dpa by it&#39;s dpaId
[**retrieve_dpa_list**](DPASApi.md#retrieve_dpa_list) | **GET** /v1/dpas | List all Dpas
[**terminate_dpa**](DPASApi.md#terminate_dpa) | **POST** /v1/dpas/{dpaId}/terminate | Terminate an existing DPA by id


# **conclude_dpa**
> DpaResponse conclude_dpa(x_request_id, dpa_id)

Concludes a data processing agreement

Concludes data processing agreement for a specific service that you own.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
from pfruck_contabo.model.dpa_response import DpaResponse
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    dpa_id = "6C65CD0E-572F-4051-9161-0D731DB44B6E" # str | The identifier of the data processing agreement
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Concludes a data processing agreement
        api_response = api_instance.conclude_dpa(x_request_id, dpa_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->conclude_dpa: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Concludes a data processing agreement
        api_response = api_instance.conclude_dpa(x_request_id, dpa_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->conclude_dpa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **dpa_id** | **str**| The identifier of the data processing agreement |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**DpaResponse**](DpaResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard data processing agreement attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dpa**
> DpaResponse create_dpa(x_request_id, create_dpa_request)

Create a new data processing agreement

Create a new data processing agreement for a specific service that you own.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
from pfruck_contabo.model.create_dpa_request import CreateDpaRequest
from pfruck_contabo.model.dpa_response import DpaResponse
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    create_dpa_request = CreateDpaRequest(
        processed_data_type=ProcessedDataType(
            billing_data=True,
            address_data=True,
            offer_data=True,
            authentication_data=True,
            bank_details=True,
            order_data=True,
            image_files=True,
            emails=True,
            financial_data=True,
            communication_data=True,
            employee_data=True,
            usage_data=True,
            password_data=True,
            personnel_data=True,
            personnel_master_data=True,
            program_code=True,
            profile_data=True,
            transaction_data=True,
            contract_data=True,
            contract_billing_data=True,
            video_files=True,
            payment_data=True,
            ip_addresses=True,
            other=OtherData(
                value=True,
                text="Other",
            ),
        ),
        personal_data=PersonalData(
            biometric_data=True,
            genetic_data=True,
            health_data=True,
            political_opinion_data=True,
            racial_and_ethnic_origin_data=True,
            religious_and_philosophical_beliefs_data=True,
            labor_organization_membership_data=True,
            sexual_life_data=True,
            personality_data=True,
        ),
        affected_persons=AffectedPersons(
            subscribers=True,
            relatives=True,
            trainees=True,
            applicants=True,
            consultants=True,
            service_providers=True,
            former_employees=True,
            aggrieved_parties=True,
            business_partners=True,
            shareholders=True,
            commercial_agents=True,
            interested_parties=True,
            customers=True,
            suppliers=True,
            brokers_or_intermediaries=True,
            tenants=True,
            employees=True,
            members=True,
            users=True,
            interns=True,
            dependents=True,
            press=True,
            witnesses=True,
            other=OtherData(
                value=True,
                text="Other",
            ),
        ),
        data_protection_officer=DataProtectionOfficerRequest(
            email="test@contabo.de",
            first_name="John",
            last_name="Doe",
            address=DataProtectionOfficerRequestAddress(None),
            phone_number="+49 30 901820",
        ),
        dpa_service_id="1",
    ) # CreateDpaRequest | 
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new data processing agreement
        api_response = api_instance.create_dpa(x_request_id, create_dpa_request)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->create_dpa: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new data processing agreement
        api_response = api_instance.create_dpa(x_request_id, create_dpa_request, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->create_dpa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **create_dpa_request** | [**CreateDpaRequest**](CreateDpaRequest.md)|  |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**DpaResponse**](DpaResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response will be a JSON object and contains standard data processing agreement attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dpa_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_dpa_file(x_request_id, dpa_id)

Download concluded DPA PDF file

Download the data processing agreement PDF file

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    dpa_id = "6C65CD0E-572F-4051-9161-0D731DB44B6E" # str | The identifier of the data processing agreement
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    action = "preview" # str | Set the action for download PDF or only preview it. Default is preview (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download concluded DPA PDF file
        api_response = api_instance.download_dpa_file(x_request_id, dpa_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->download_dpa_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download concluded DPA PDF file
        api_response = api_instance.download_dpa_file(x_request_id, dpa_id, x_trace_id=x_trace_id, action=action)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->download_dpa_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **dpa_id** | **str**| The identifier of the data processing agreement |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **action** | **str**| Set the action for download PDF or only preview it. Default is preview | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a binary stream of your data processing agreement PDF |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_preview_dpa**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download_preview_dpa(x_request_id, dpa_id)

Download preview version of DPA

Obtain a preview version pdf of the DPA.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    dpa_id = "6C65CD0E-572F-4051-9161-0D731DB44B6E" # str | The identifier of the data processing agreement
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Download preview version of DPA
        api_response = api_instance.download_preview_dpa(x_request_id, dpa_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->download_preview_dpa: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download preview version of DPA
        api_response = api_instance.download_preview_dpa(x_request_id, dpa_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->download_preview_dpa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **dpa_id** | **str**| The identifier of the data processing agreement |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a pdf stream. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dpa_services**
> ListDpaServicesResponse list_dpa_services(x_request_id)

List services

List all services for which you can create a data processing agreement

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
from pfruck_contabo.model.list_dpa_services_response import ListDpaServicesResponse
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "serviceName:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. Possible fields: `serviceName`, `ipAddress`, `displayName` (optional)
    search = "MyVps2" # str | Filter services by `serviceName`, `ipAddress` or `displayName` (optional)
    has_concluded_dpa = "false" # str | Filters services which already have a concluded DPA (hasConcludedDpa=true) or not (hasConcludedDpa=false) (optional)

    # example passing only required values which don't have defaults set
    try:
        # List services
        api_response = api_instance.list_dpa_services(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->list_dpa_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List services
        api_response = api_instance.list_dpa_services(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, search=search, has_concluded_dpa=has_concluded_dpa)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->list_dpa_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. Possible fields: &#x60;serviceName&#x60;, &#x60;ipAddress&#x60;, &#x60;displayName&#x60; | [optional]
 **search** | **str**| Filter services by &#x60;serviceName&#x60;, &#x60;ipAddress&#x60; or &#x60;displayName&#x60; | [optional]
 **has_concluded_dpa** | **str**| Filters services which already have a concluded DPA (hasConcludedDpa&#x3D;true) or not (hasConcludedDpa&#x3D;false) | [optional]

### Return type

[**ListDpaServicesResponse**](ListDpaServicesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all services for which you can create a data processing agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dpa**
> DpaResponse retrieve_dpa(x_request_id, dpa_id)

Get specific Dpa by it's dpaId

Get data for a specific Dpa on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
from pfruck_contabo.model.dpa_response import DpaResponse
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    dpa_id = "6C65CD0E-572F-4051-9161-0D731DB44B6E" # str | The identifier of the data processing agreement
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get specific Dpa by it's dpaId
        api_response = api_instance.retrieve_dpa(x_request_id, dpa_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->retrieve_dpa: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get specific Dpa by it's dpaId
        api_response = api_instance.retrieve_dpa(x_request_id, dpa_id, x_trace_id=x_trace_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->retrieve_dpa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **dpa_id** | **str**| The identifier of the data processing agreement |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]

### Return type

[**DpaResponse**](DpaResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object and contains standard Dpa attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dpa_list**
> ListDpaResponse retrieve_dpa_list(x_request_id)

List all Dpas

List and filter all Dpas on your account.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
from pfruck_contabo.model.list_dpa_response import ListDpaResponse
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)
    page = 1 # int | Number of page to be fetched. (optional)
    size = 10 # int | Number of elements per page. (optional)
    order_by = [
        "name:asc",
    ] # [str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
    status = "preview" # str | The status of the Dpa (optional) if omitted the server will use the default value of "concluded,invalid"
    search = "preview" # str | Filter dpas by `serviceName`, `dpaId` or `status` (optional)
    dpa_service_id = "true" # str | The dpaServiceId by which we want to filter the Dpas (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all Dpas
        api_response = api_instance.retrieve_dpa_list(x_request_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->retrieve_dpa_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Dpas
        api_response = api_instance.retrieve_dpa_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, status=status, search=search, dpa_service_id=dpa_service_id)
        pprint(api_response)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->retrieve_dpa_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **x_trace_id** | **str**| Identifier to trace group of requests. | [optional]
 **page** | **int**| Number of page to be fetched. | [optional]
 **size** | **int**| Number of elements per page. | [optional]
 **order_by** | **[str]**| Specify fields and ordering (ASC for ascending, DESC for descending) in following format &#x60;field:ASC|DESC&#x60;. | [optional]
 **status** | **str**| The status of the Dpa | [optional] if omitted the server will use the default value of "concluded,invalid"
 **search** | **str**| Filter dpas by &#x60;serviceName&#x60;, &#x60;dpaId&#x60; or &#x60;status&#x60; | [optional]
 **dpa_service_id** | **str**| The dpaServiceId by which we want to filter the Dpas | [optional]

### Return type

[**ListDpaResponse**](ListDpaResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response will be a JSON object which will contain a paginated list of Dpas. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_dpa**
> terminate_dpa(x_request_id, dpa_id)

Terminate an existing DPA by id

Terminate an existing DPA for a specific service by id.

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import pfruck_contabo
from pfruck_contabo.api import dpas_api
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
    api_instance = dpas_api.DPASApi(api_client)
    x_request_id = "04e0f898-37b4-48bc-a794-1a57abe6aa31" # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
    dpa_id = "6C65CD0E-572F-4051-9161-0D731DB44B6E" # str | The identifier of the data processing agreement
    x_trace_id = "x-trace-id_example" # str | Identifier to trace group of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Terminate an existing DPA by id
        api_instance.terminate_dpa(x_request_id, dpa_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->terminate_dpa: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Terminate an existing DPA by id
        api_instance.terminate_dpa(x_request_id, dpa_id, x_trace_id=x_trace_id)
    except pfruck_contabo.ApiException as e:
        print("Exception when calling DPASApi->terminate_dpa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. |
 **dpa_id** | **str**| The identifier of the data processing agreement |
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

