# ListFirewallResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**firewall_id** | **str** | Your firewall id. | 
**name** | **str** | The name of the firewall. | 
**description** | **str** | The description of the firewall. | 
**status** | **str** | Inactive status means no rules of this firewall are set for all assigned instances. | 
**instance_status** | [**List[InstanceStatusRepresentation]**](InstanceStatusRepresentation.md) |  | 
**instances** | [**List[InstanceDetails]**](InstanceDetails.md) |  | 
**rules** | [**Rules**](Rules.md) |  | 
**created_date** | **datetime** | The creation date time for the firewall | 
**updated_date** | **datetime** | The update date time for the firewall | 

## Example

```python
from pfruck_contabo.models.list_firewall_response_data import ListFirewallResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallResponseData from a JSON string
list_firewall_response_data_instance = ListFirewallResponseData.from_json(json)
# print the JSON string representation of the object
print(ListFirewallResponseData.to_json())

# convert the object into a dict
list_firewall_response_data_dict = list_firewall_response_data_instance.to_dict()
# create an instance of ListFirewallResponseData from a dict
list_firewall_response_data_from_dict = ListFirewallResponseData.from_dict(list_firewall_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


