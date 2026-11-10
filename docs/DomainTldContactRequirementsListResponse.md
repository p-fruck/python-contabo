# DomainTldContactRequirementsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainTldContactRequirementsResponse]**](DomainTldContactRequirementsResponse.md) | The TLDs Contabo sells whose contacts need more than the standard handle fields, sorted by TLD. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_tld_contact_requirements_list_response import DomainTldContactRequirementsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldContactRequirementsListResponse from a JSON string
domain_tld_contact_requirements_list_response_instance = DomainTldContactRequirementsListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldContactRequirementsListResponse.to_json())

# convert the object into a dict
domain_tld_contact_requirements_list_response_dict = domain_tld_contact_requirements_list_response_instance.to_dict()
# create an instance of DomainTldContactRequirementsListResponse from a dict
domain_tld_contact_requirements_list_response_from_dict = DomainTldContactRequirementsListResponse.from_dict(domain_tld_contact_requirements_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


