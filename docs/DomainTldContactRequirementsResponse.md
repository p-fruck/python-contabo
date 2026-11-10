# DomainTldContactRequirementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**tld** | **str** | The TLD the requirements apply to. | 
**roles** | [**List[DomainTldContactRoleResponse]**](DomainTldContactRoleResponse.md) | Contact roles the registry accepts, with how many contacts of each a domain needs. | 
**attributes** | [**List[DomainTldContactAttributeResponse]**](DomainTldContactAttributeResponse.md) | Registry-specific contact attributes on top of the standard handle fields. Empty when the TLD defines none. | 
**local_presence** | [**DomainTldContactRequirementsResponseLocalPresence**](DomainTldContactRequirementsResponseLocalPresence.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_tld_contact_requirements_response import DomainTldContactRequirementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldContactRequirementsResponse from a JSON string
domain_tld_contact_requirements_response_instance = DomainTldContactRequirementsResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldContactRequirementsResponse.to_json())

# convert the object into a dict
domain_tld_contact_requirements_response_dict = domain_tld_contact_requirements_response_instance.to_dict()
# create an instance of DomainTldContactRequirementsResponse from a dict
domain_tld_contact_requirements_response_from_dict = DomainTldContactRequirementsResponse.from_dict(domain_tld_contact_requirements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


