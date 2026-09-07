# CreateFirewallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the firewall. | 
**description** | **str** | The description of the firewall. | [optional] 
**status** | **str** | The status of the firewall determines whether the rules are active or not. | 
**rules** | [**RulesRequest**](RulesRequest.md) |  | [optional] 

## Example

```python
from pfruck_contabo.models.create_firewall_request import CreateFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRequest from a JSON string
create_firewall_request_instance = CreateFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRequest.to_json())

# convert the object into a dict
create_firewall_request_dict = create_firewall_request_instance.to_dict()
# create an instance of CreateFirewallRequest from a dict
create_firewall_request_from_dict = CreateFirewallRequest.from_dict(create_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


