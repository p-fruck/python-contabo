# PutFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FirewallResponse]**](FirewallResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.put_firewall_response import PutFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutFirewallResponse from a JSON string
put_firewall_response_instance = PutFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(PutFirewallResponse.to_json())

# convert the object into a dict
put_firewall_response_dict = put_firewall_response_instance.to_dict()
# create an instance of PutFirewallResponse from a dict
put_firewall_response_from_dict = PutFirewallResponse.from_dict(put_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


