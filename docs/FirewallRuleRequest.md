# FirewallRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Protocol for incoming traffic to be allowed. ‘tcp‘, ´udp´, ´icmp´ or ´´ empty value are allowed. Empty means any traffic. | 
**dest_ports** | **List[str]** | Ports to specify allowed traffic. Not available for protocol &#x60;ICMP&#x60;. Port ranges can specified like in example. | 
**src_cidr** | [**SrcCidr**](SrcCidr.md) | Source CIDR configuration. Use \&quot;AnyIPv4\&quot; to allow all IPv4 sources (0.0.0.0/0) or \&quot;AnyIPv6\&quot; to allow all IPv6 sources (::/0). Both can be combined to allow all IP sources. Regular CIDR notation is also supported. | 
**action** | **str** | Currently only &#x60;accept&#x60; is supported. | 
**status** | **str** | Status of the inbound rule. An inactive rule is removed from all assigned instances. | 
**display_name** | **str** | Display name for the firewall rule. | [optional] 

## Example

```python
from pfruck_contabo.models.firewall_rule_request import FirewallRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleRequest from a JSON string
firewall_rule_request_instance = FirewallRuleRequest.from_json(json)
# print the JSON string representation of the object
print(FirewallRuleRequest.to_json())

# convert the object into a dict
firewall_rule_request_dict = firewall_rule_request_instance.to_dict()
# create an instance of FirewallRuleRequest from a dict
firewall_rule_request_from_dict = FirewallRuleRequest.from_dict(firewall_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


