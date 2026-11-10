# DomainTldContactRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Contact role: &#x60;registrant&#x60;, &#x60;admin&#x60;, &#x60;tech&#x60; or &#x60;billing&#x60;. A role not listed cannot be set for this TLD. | 
**min** | **float** | Minimum number of contacts of this role per domain. 0 means optional. | 
**max** | **float** | Maximum number of contacts of this role per domain. | 

## Example

```python
from pfruck_contabo.models.domain_tld_contact_role_response import DomainTldContactRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldContactRoleResponse from a JSON string
domain_tld_contact_role_response_instance = DomainTldContactRoleResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldContactRoleResponse.to_json())

# convert the object into a dict
domain_tld_contact_role_response_dict = domain_tld_contact_role_response_instance.to_dict()
# create an instance of DomainTldContactRoleResponse from a dict
domain_tld_contact_role_response_from_dict = DomainTldContactRoleResponse.from_dict(domain_tld_contact_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


