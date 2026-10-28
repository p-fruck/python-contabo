# PutFirewallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**RulesRequest**](RulesRequest.md) |  | [optional] 

## Example

```python
from pfruck_contabo.models.put_firewall_request import PutFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFirewallRequest from a JSON string
put_firewall_request_instance = PutFirewallRequest.from_json(json)
# print the JSON string representation of the object
print(PutFirewallRequest.to_json())

# convert the object into a dict
put_firewall_request_dict = put_firewall_request_instance.to_dict()
# create an instance of PutFirewallRequest from a dict
put_firewall_request_from_dict = PutFirewallRequest.from_dict(put_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


