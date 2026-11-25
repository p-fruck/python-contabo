# DomainTldAttributeConditionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Key of the contact attribute the condition evaluates. | 
**operator** | **str** | Comparison operator: &#x60;equals&#x60;, &#x60;not_equals&#x60;, &#x60;in&#x60; or &#x60;not_in&#x60;. | 
**values** | **List[str]** | Values the attribute is compared with. &#x60;equals&#x60; and &#x60;not_equals&#x60; carry exactly one. | 

## Example

```python
from pfruck_contabo.models.domain_tld_attribute_condition_response import DomainTldAttributeConditionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTldAttributeConditionResponse from a JSON string
domain_tld_attribute_condition_response_instance = DomainTldAttributeConditionResponse.from_json(json)
# print the JSON string representation of the object
print(DomainTldAttributeConditionResponse.to_json())

# convert the object into a dict
domain_tld_attribute_condition_response_dict = domain_tld_attribute_condition_response_instance.to_dict()
# create an instance of DomainTldAttributeConditionResponse from a dict
domain_tld_attribute_condition_response_from_dict = DomainTldAttributeConditionResponse.from_dict(domain_tld_attribute_condition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


