# AssignInstanceFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InstanceAssignmentSelfLinks1**](InstanceAssignmentSelfLinks1.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.assign_instance_firewall_response import AssignInstanceFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignInstanceFirewallResponse from a JSON string
assign_instance_firewall_response_instance = AssignInstanceFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(AssignInstanceFirewallResponse.to_json())

# convert the object into a dict
assign_instance_firewall_response_dict = assign_instance_firewall_response_instance.to_dict()
# create an instance of AssignInstanceFirewallResponse from a dict
assign_instance_firewall_response_from_dict = AssignInstanceFirewallResponse.from_dict(assign_instance_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


