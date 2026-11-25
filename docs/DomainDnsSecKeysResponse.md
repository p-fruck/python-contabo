# DomainDnsSecKeysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainResponse]**](DomainResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_dns_sec_keys_response import DomainDnsSecKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDnsSecKeysResponse from a JSON string
domain_dns_sec_keys_response_instance = DomainDnsSecKeysResponse.from_json(json)
# print the JSON string representation of the object
print(DomainDnsSecKeysResponse.to_json())

# convert the object into a dict
domain_dns_sec_keys_response_dict = domain_dns_sec_keys_response_instance.to_dict()
# create an instance of DomainDnsSecKeysResponse from a dict
domain_dns_sec_keys_response_from_dict = DomainDnsSecKeysResponse.from_dict(domain_dns_sec_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


