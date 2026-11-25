# DomainSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**domain** | **str** | Suggested fully-qualified domain name. | 
**available** | **bool** | Whether the suggested domain is available for registration. | 
**premium** | **bool** | Whether the suggested domain is premium-priced. | 

## Example

```python
from pfruck_contabo.models.domain_suggestion import DomainSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of DomainSuggestion from a JSON string
domain_suggestion_instance = DomainSuggestion.from_json(json)
# print the JSON string representation of the object
print(DomainSuggestion.to_json())

# convert the object into a dict
domain_suggestion_dict = domain_suggestion_instance.to_dict()
# create an instance of DomainSuggestion from a dict
domain_suggestion_from_dict = DomainSuggestion.from_dict(domain_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


