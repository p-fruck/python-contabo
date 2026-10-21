# PatchFirewallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the firewall | [optional] 
**status** | **str** | Active status of the firewall enables all rules, thus filtering traffic. Inactive status does not filter any traffic. | [optional] 
**description** | **str** | The description of the firewall. | [optional] 

## Example

```python
from pfruck_contabo.models.patch_firewall_request import PatchFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallRequest from a JSON string
patch_firewall_request_instance = PatchFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallRequest.to_json())

# convert the object into a dict
patch_firewall_request_dict = patch_firewall_request_instance.to_dict()
# create an instance of PatchFirewallRequest from a dict
patch_firewall_request_from_dict = PatchFirewallRequest.from_dict(patch_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


