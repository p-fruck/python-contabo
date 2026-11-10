# DomainTldContactRequirementsFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainTldContactRequirementsResponse]**](DomainTldContactRequirementsResponse.md) | Exactly one item: the requirements of the requested TLD. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_tld_contact_requirements_find_response import DomainTldContactRequirementsFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldContactRequirementsFindResponse from a JSON string
domain_tld_contact_requirements_find_response_instance = DomainTldContactRequirementsFindResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldContactRequirementsFindResponse.to_json())

# convert the object into a dict
domain_tld_contact_requirements_find_response_dict = domain_tld_contact_requirements_find_response_instance.to_dict()
# create an instance of DomainTldContactRequirementsFindResponse from a dict
domain_tld_contact_requirements_find_response_from_dict = DomainTldContactRequirementsFindResponse.from_dict(domain_tld_contact_requirements_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


