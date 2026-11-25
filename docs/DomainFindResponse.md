# DomainFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainResponse]**](DomainResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_find_response import DomainFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainFindResponse from a JSON string
domain_find_response_instance = DomainFindResponse.from_json(json)
# print the JSON string representation of the object
print(DomainFindResponse.to_json())

# convert the object into a dict
domain_find_response_dict = domain_find_response_instance.to_dict()
# create an instance of DomainFindResponse from a dict
domain_find_response_from_dict = DomainFindResponse.from_dict(domain_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


