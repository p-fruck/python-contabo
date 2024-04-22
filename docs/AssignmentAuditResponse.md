# AssignmentAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**id** | **float** | The identifier of the audit entry. | 
**resource_id** | **str** | Resource&#39;s id | 
**resource_type** | **str** | Resource type. Resource type is one of &#x60;instance|image|object-storage&#x60;. | 
**tag_id** | **int** | Tag&#39;s id | 
**action** | **str** | Audit Action | 
**timestamp** | **datetime** | Audit creation date | 
**changed_by** | **str** | User ID | 
**username** | **str** | User Full Name | 
**request_id** | **str** | Request ID | 
**trace_id** | **str** | Trace ID | 
**changes** | **object** | Changes made for a specific Tag | [optional] 

## Example

```python
from pfruck_contabo.models.assignment_audit_response import AssignmentAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentAuditResponse from a JSON string
assignment_audit_response_instance = AssignmentAuditResponse.from_json(json)
# print the JSON string representation of the object
print(AssignmentAuditResponse.to_json())

# convert the object into a dict
assignment_audit_response_dict = assignment_audit_response_instance.to_dict()
# create an instance of AssignmentAuditResponse from a dict
assignment_audit_response_from_dict = AssignmentAuditResponse.from_dict(assignment_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


