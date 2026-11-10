# DomainTldContactRequirementsResponseLocalPresence

The local-presence rule, or null when the registry declares none.

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
from pfruck_contabo.models.domain_tld_contact_requirements_response_local_presence import DomainTldContactRequirementsResponseLocalPresence

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldContactRequirementsResponseLocalPresence from a JSON string
domain_tld_contact_requirements_response_local_presence_instance = DomainTldContactRequirementsResponseLocalPresence.from_json(json)
# print the JSON string representation of the object
print(DomainTldContactRequirementsResponseLocalPresence.to_json())

# convert the object into a dict
domain_tld_contact_requirements_response_local_presence_dict = domain_tld_contact_requirements_response_local_presence_instance.to_dict()
# create an instance of DomainTldContactRequirementsResponseLocalPresence from a dict
domain_tld_contact_requirements_response_local_presence_from_dict = DomainTldContactRequirementsResponseLocalPresence.from_dict(domain_tld_contact_requirements_response_local_presence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


