# VipAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the audit entry. | 
**vip_id** | **str** | The identifier of the VIP | 
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
from pfruck_contabo.models.vip_audit_response import VipAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VipAuditResponse from a JSON string
vip_audit_response_instance = VipAuditResponse.from_json(json)
# print the JSON string representation of the object
print(VipAuditResponse.to_json())

# convert the object into a dict
vip_audit_response_dict = vip_audit_response_instance.to_dict()
# create an instance of VipAuditResponse from a dict
vip_audit_response_from_dict = VipAuditResponse.from_dict(vip_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


