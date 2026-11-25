# DomainCancel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**domain** | **str** | Domain name | 
**sld** | **str** | Domain SLD | 
**tld** | **str** | Domain TLD | 
**cancel_date** | **datetime** | The cancel date of domain | 

## Example

```python
from pfruck_contabo.models.domain_cancel import DomainCancel

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCancel from a JSON string
domain_cancel_instance = DomainCancel.from_json(json)
# print the JSON string representation of the object
print(DomainCancel.to_json())

# convert the object into a dict
domain_cancel_dict = domain_cancel_instance.to_dict()
# create an instance of DomainCancel from a dict
domain_cancel_from_dict = DomainCancel.from_dict(domain_cancel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


