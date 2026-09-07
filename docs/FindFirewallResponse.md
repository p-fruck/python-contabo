# FindFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FirewallResponse]**](FirewallResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_firewall_response import FindFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindFirewallResponse from a JSON string
find_firewall_response_instance = FindFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(FindFirewallResponse.to_json())

# convert the object into a dict
find_firewall_response_dict = find_firewall_response_instance.to_dict()
# create an instance of FindFirewallResponse from a dict
find_firewall_response_from_dict = FindFirewallResponse.from_dict(find_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


