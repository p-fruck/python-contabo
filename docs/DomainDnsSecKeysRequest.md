# DomainDnsSecKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_sec_keys** | **List[str]** | DNSSEC keys | 

## Example

```python
from pfruck_contabo.models.domain_dns_sec_keys_request import DomainDnsSecKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDnsSecKeysRequest from a JSON string
domain_dns_sec_keys_request_instance = DomainDnsSecKeysRequest.from_json(json)
# print the JSON string representation of the object
print(DomainDnsSecKeysRequest.to_json())

# convert the object into a dict
domain_dns_sec_keys_request_dict = domain_dns_sec_keys_request_instance.to_dict()
# create an instance of DomainDnsSecKeysRequest from a dict
domain_dns_sec_keys_request_from_dict = DomainDnsSecKeysRequest.from_dict(domain_dns_sec_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


