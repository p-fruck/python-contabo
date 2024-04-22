# PrivateNetworkAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the audit entry. | 
**private_network_id** | **float** | The identifier of the Private Network | 
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
from pfruck_contabo.models.private_network_audit_response import PrivateNetworkAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkAuditResponse from a JSON string
private_network_audit_response_instance = PrivateNetworkAuditResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkAuditResponse.to_json())

# convert the object into a dict
private_network_audit_response_dict = private_network_audit_response_instance.to_dict()
# create an instance of PrivateNetworkAuditResponse from a dict
private_network_audit_response_from_dict = PrivateNetworkAuditResponse.from_dict(private_network_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


