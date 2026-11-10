# FirewallAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the audit entry. | 
**firewall_id** | **str** | The identifier of the Firewall | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**tenant_id** | **str** | Customer tenant id | 
**customer_id** | **str** | Customer number | 
**changed_by** | **str** | User id | 
**username** | **str** | User name which did the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.firewall_audit_response import FirewallAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallAuditResponse from a JSON string
firewall_audit_response_instance = FirewallAuditResponse.from_json(json)
# print the JSON string representation of the object
print(FirewallAuditResponse.to_json())

# convert the object into a dict
firewall_audit_response_dict = firewall_audit_response_instance.to_dict()
# create an instance of FirewallAuditResponse from a dict
firewall_audit_response_from_dict = FirewallAuditResponse.from_dict(firewall_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


