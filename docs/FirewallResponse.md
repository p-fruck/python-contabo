# FirewallResponse


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
from pfruck_contabo.models.firewall_response import FirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallResponse from a JSON string
firewall_response_instance = FirewallResponse.from_json(json)
# print the JSON string representation of the object
print(FirewallResponse.to_json())

# convert the object into a dict
firewall_response_dict = firewall_response_instance.to_dict()
# create an instance of FirewallResponse from a dict
firewall_response_from_dict = FirewallResponse.from_dict(firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


