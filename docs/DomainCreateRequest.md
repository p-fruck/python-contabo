# DomainCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | 
**auth_code** | **str** | The domain auth code | [optional] 
**handles** | [**DomainHandles**](DomainHandles.md) | The handles of the domain | 
**nameservers** | [**List[Nameserver]**](Nameserver.md) | Nameservers | 
**resource_type** | **str** | The identifier of the resource type | [optional] 
**resource_id** | **str** | The identifier of the resource id | [optional] 

## Example

```python
from pfruck_contabo.models.domain_create_request import DomainCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreateRequest from a JSON string
domain_create_request_instance = DomainCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainCreateRequest.to_json())

# convert the object into a dict
domain_create_request_dict = domain_create_request_instance.to_dict()
# create an instance of DomainCreateRequest from a dict
domain_create_request_from_dict = DomainCreateRequest.from_dict(domain_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


