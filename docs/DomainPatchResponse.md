# DomainPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainResponse]**](DomainResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_patch_response import DomainPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPatchResponse from a JSON string
domain_patch_response_instance = DomainPatchResponse.from_json(json)
# print the JSON string representation of the object
print(DomainPatchResponse.to_json())

# convert the object into a dict
domain_patch_response_dict = domain_patch_response_instance.to_dict()
# create an instance of DomainPatchResponse from a dict
domain_patch_response_from_dict = DomainPatchResponse.from_dict(domain_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


