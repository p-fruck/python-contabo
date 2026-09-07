# DomainAuthCodeResponse


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
**auth_code** | **str** | Your auth code of the domain | 
**auth_code_changed** | [**ChangedAuthCode**](ChangedAuthCode.md) | Details if the auth code has been changed | 

## Example

```python
from pfruck_contabo.models.domain_auth_code_response import DomainAuthCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAuthCodeResponse from a JSON string
domain_auth_code_response_instance = DomainAuthCodeResponse.from_json(json)
# print the JSON string representation of the object
print(DomainAuthCodeResponse.to_json())

# convert the object into a dict
domain_auth_code_response_dict = domain_auth_code_response_instance.to_dict()
# create an instance of DomainAuthCodeResponse from a dict
domain_auth_code_response_from_dict = DomainAuthCodeResponse.from_dict(domain_auth_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


