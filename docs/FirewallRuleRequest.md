# FirewallRuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Protocol for incoming traffic to be allowed. ‘tcp‘, ´udp´, ´icmp´ or ´´ empty value are allowed. Empty means any traffic. | 
**dest_ports** | **[str]** | Ports to specify allowed traffic. Not available for protocol &#x60;ICMP&#x60;. Port ranges can specified like in example. | 
**src_cidr** | [**SrcCidr**](SrcCidr.md) |  | 
**action** | **str** | Currently only &#x60;accept&#x60; is supported. | 
**status** | **str** | Status of the inbound rule. An inactive rule is removed from all assigned instances. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


