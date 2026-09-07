# DomainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**domain** | **str** | Domain name | 
**domain_details** | [**DomainDetails**](DomainDetails.md) | Domain Details | 
**status** | **str** | Domain Status | 
**nameservers** | **List[str]** | Nameservers | 
**handles** | [**DomainHandles**](DomainHandles.md) | The handles of the domain | 
**registration_date** | **datetime** | The registration date of domain | 
**renewal_date** | **datetime** | The renewal date of domain | 
**termination_date** | **datetime** | The termination date of domain | 
**cancel_date** | **datetime** | The cancel date of domain | 
**dnssec_keys** | **List[str]** | DNSSEC keys | 
**transfer_out_confirmation** | **bool** | Transfer out confirmation | 
**status_error** | [**DomainResponseStatusError**](DomainResponseStatusError.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_response import DomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponse from a JSON string
domain_response_instance = DomainResponse.from_json(json)
# print the JSON string representation of the object
print(DomainResponse.to_json())

# convert the object into a dict
domain_response_dict = domain_response_instance.to_dict()
# create an instance of DomainResponse from a dict
domain_response_from_dict = DomainResponse.from_dict(domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


