# DomainPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameservers** | [**List[Nameserver]**](Nameserver.md) | Nameservers | [optional] 
**handles** | [**DomainHandles**](DomainHandles.md) | The handles of the domain | [optional] 

## Example

```python
from pfruck_contabo.models.domain_patch_request import DomainPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPatchRequest from a JSON string
domain_patch_request_instance = DomainPatchRequest.from_json(json)
# print the JSON string representation of the object
print(DomainPatchRequest.to_json())

# convert the object into a dict
domain_patch_request_dict = domain_patch_request_instance.to_dict()
# create an instance of DomainPatchRequest from a dict
domain_patch_request_from_dict = DomainPatchRequest.from_dict(domain_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


