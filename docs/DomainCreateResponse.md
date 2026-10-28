# DomainCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainResponse]**](DomainResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_create_response import DomainCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreateResponse from a JSON string
domain_create_response_instance = DomainCreateResponse.from_json(json)
# print the JSON string representation of the object
print(DomainCreateResponse.to_json())

# convert the object into a dict
domain_create_response_dict = domain_create_response_instance.to_dict()
# create an instance of DomainCreateResponse from a dict
domain_create_response_from_dict = DomainCreateResponse.from_dict(domain_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


