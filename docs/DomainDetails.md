# DomainDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sld** | **str** | Domain SLD | 
**tld** | **str** | Domain TLD | 
**domain_puny** | **str** | Domain Puny | 

## Example

```python
from pfruck_contabo.models.domain_details import DomainDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDetails from a JSON string
domain_details_instance = DomainDetails.from_json(json)
# print the JSON string representation of the object
print(DomainDetails.to_json())

# convert the object into a dict
domain_details_dict = domain_details_instance.to_dict()
# create an instance of DomainDetails from a dict
domain_details_from_dict = DomainDetails.from_dict(domain_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


