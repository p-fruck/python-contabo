# ListFirewallAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[FirewallAuditResponse]**](FirewallAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_firewall_audit_response import ListFirewallAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallAuditResponse from a JSON string
list_firewall_audit_response_instance = ListFirewallAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ListFirewallAuditResponse.to_json())

# convert the object into a dict
list_firewall_audit_response_dict = list_firewall_audit_response_instance.to_dict()
# create an instance of ListFirewallAuditResponse from a dict
list_firewall_audit_response_from_dict = ListFirewallAuditResponse.from_dict(list_firewall_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


