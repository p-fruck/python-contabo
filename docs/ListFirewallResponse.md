# ListFirewallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ListFirewallResponseData]**](ListFirewallResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_firewall_response import ListFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallResponse from a JSON string
list_firewall_response_instance = ListFirewallResponse.from_json(json)
# print the JSON string representation of the object
print(ListFirewallResponse.to_json())

# convert the object into a dict
list_firewall_response_dict = list_firewall_response_instance.to_dict()
# create an instance of ListFirewallResponse from a dict
list_firewall_response_from_dict = ListFirewallResponse.from_dict(list_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


