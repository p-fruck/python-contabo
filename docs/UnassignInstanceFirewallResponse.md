# UnassignInstanceFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InstanceAssignmentSelfLinks1**](InstanceAssignmentSelfLinks1.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.unassign_instance_firewall_response import UnassignInstanceFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignInstanceFirewallResponse from a JSON string
unassign_instance_firewall_response_instance = UnassignInstanceFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(UnassignInstanceFirewallResponse.to_json())

# convert the object into a dict
unassign_instance_firewall_response_dict = unassign_instance_firewall_response_instance.to_dict()
# create an instance of UnassignInstanceFirewallResponse from a dict
unassign_instance_firewall_response_from_dict = UnassignInstanceFirewallResponse.from_dict(unassign_instance_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


