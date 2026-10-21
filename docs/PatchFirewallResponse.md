# PatchFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FirewallResponse]**](FirewallResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.patch_firewall_response import PatchFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallResponse from a JSON string
patch_firewall_response_instance = PatchFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallResponse.to_json())

# convert the object into a dict
patch_firewall_response_dict = patch_firewall_response_instance.to_dict()
# create an instance of PatchFirewallResponse from a dict
patch_firewall_response_from_dict = PatchFirewallResponse.from_dict(patch_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


