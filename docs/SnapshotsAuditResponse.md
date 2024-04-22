# SnapshotsAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the audit entry. | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**tenant_id** | **str** | Customer tenant id | 
**customer_id** | **str** | Customer ID | 
**changed_by** | **str** | Id of user who performed the change | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**instance_id** | **int** | The identifier of the instance | 
**snapshot_id** | **str** | The identifier of the snapshot | 
**changes** | **object** | List of actual changes | [optional] 

## Example

```python
from pfruck_contabo.models.snapshots_audit_response import SnapshotsAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotsAuditResponse from a JSON string
snapshots_audit_response_instance = SnapshotsAuditResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotsAuditResponse.to_json())

# convert the object into a dict
snapshots_audit_response_dict = snapshots_audit_response_instance.to_dict()
# create an instance of SnapshotsAuditResponse from a dict
snapshots_audit_response_from_dict = SnapshotsAuditResponse.from_dict(snapshots_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


