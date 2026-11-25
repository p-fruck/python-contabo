# DomainTldContactAttributeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Registry attribute key. | 
**type** | **str** | Value type: &#x60;enum&#x60;, &#x60;string&#x60;, &#x60;boolean&#x60;, &#x60;datetime&#x60;, &#x60;integer&#x60;, &#x60;country_code&#x60; or &#x60;uri_template&#x60;. | 
**required** | **bool** | Whether the attribute must be set when it applies (see &#x60;conditions&#x60;). | 
**values** | **List[str]** | Allowed values of an &#x60;enum&#x60; attribute; empty otherwise. | 
**roles** | **List[str]** | Contact roles the attribute applies to. | 
**conditions** | [**List[DomainTldAttributeConditionResponse]**](DomainTldAttributeConditionResponse.md) | Conditions that must ALL hold for the attribute to apply. Empty means it always applies. | 

## Example

```python
from pfruck_contabo.models.domain_tld_contact_attribute_response import DomainTldContactAttributeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldContactAttributeResponse from a JSON string
domain_tld_contact_attribute_response_instance = DomainTldContactAttributeResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldContactAttributeResponse.to_json())

# convert the object into a dict
domain_tld_contact_attribute_response_dict = domain_tld_contact_attribute_response_instance.to_dict()
# create an instance of DomainTldContactAttributeResponse from a dict
domain_tld_contact_attribute_response_from_dict = DomainTldContactAttributeResponse.from_dict(domain_tld_contact_attribute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


