# FirewallRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Protocol for incoming traffic to be allowed. ‘tcp‘, ´udp´, ´icmp´ or ´´ empty value are allowed. Empty means any traffic. | 
**dest_ports** | **List[str]** | Ports to specify allowed traffic. Not available for protocol &#x60;ICMP&#x60;. Port ranges can specified like in example. | 
**src_cidr** | [**SrcCidr**](SrcCidr.md) |  | 
**action** | **str** | Currently only &#x60;accept&#x60; is supported. | 
**status** | **str** | Status of the inbound rule. An inactive rule is removed from all assigned instances. | 
**display_name** | **str** | Display name for the firewall rule. | 

## Example

```python
from pfruck_contabo.models.firewall_rule_response import FirewallRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleResponse from a JSON string
firewall_rule_response_instance = FirewallRuleResponse.from_json(json)
# print the JSON string representation of the object
print(FirewallRuleResponse.to_json())

# convert the object into a dict
firewall_rule_response_dict = firewall_rule_response_instance.to_dict()
# create an instance of FirewallRuleResponse from a dict
firewall_rule_response_from_dict = FirewallRuleResponse.from_dict(firewall_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


