# DomainHandles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | Domain&#39;s owner handle | 
**admin** | **str** | Domain&#39;s admin handle | 
**tech** | **str** | Domain&#39;s tech handle | 
**zone** | **str** | Domain&#39;s zone handle | 

## Example

```python
from pfruck_contabo.models.domain_handles import DomainHandles

# TODO update the JSON string below
json = "{}"
# create an instance of DomainHandles from a JSON string
domain_handles_instance = DomainHandles.from_json(json)
# print the JSON string representation of the object
print(DomainHandles.to_json())

# convert the object into a dict
domain_handles_dict = domain_handles_instance.to_dict()
# create an instance of DomainHandles from a dict
domain_handles_from_dict = DomainHandles.from_dict(domain_handles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


