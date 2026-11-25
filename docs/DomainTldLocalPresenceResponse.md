# DomainTldLocalPresenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | Whether a local presence is required to register and keep a domain. | 
**roles** | **List[str]** | Contact roles that must meet the requirement. | 
**requirements** | **List[str]** | Kinds of local presence accepted: &#x60;physical_address&#x60; and/or &#x60;business_entity&#x60;. | 
**eligible_countries** | **List[str]** | ISO 3166-1 alpha-2 codes of the eligible countries. Empty means the registry names none. | 
**exemptions** | [**List[DomainTldAttributeConditionResponse]**](DomainTldAttributeConditionResponse.md) | Conditions that, when ALL hold, exempt a contact from the requirement. | 

## Example

```python
from pfruck_contabo.models.domain_tld_local_presence_response import DomainTldLocalPresenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldLocalPresenceResponse from a JSON string
domain_tld_local_presence_response_instance = DomainTldLocalPresenceResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldLocalPresenceResponse.to_json())

# convert the object into a dict
domain_tld_local_presence_response_dict = domain_tld_local_presence_response_instance.to_dict()
# create an instance of DomainTldLocalPresenceResponse from a dict
domain_tld_local_presence_response_from_dict = DomainTldLocalPresenceResponse.from_dict(domain_tld_local_presence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


