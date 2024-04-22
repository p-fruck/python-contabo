# UserAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the audit entry. | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**tenant_id** | **str** | Customer tenant id | 
**customer_id** | **str** | Customer number | 
**changed_by** | **str** | User ID | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**user_id** | **str** | The identifier of the user | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.user_audit_response import UserAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserAuditResponse from a JSON string
user_audit_response_instance = UserAuditResponse.from_json(json)
# print the JSON string representation of the object
print(UserAuditResponse.to_json())

# convert the object into a dict
user_audit_response_dict = user_audit_response_instance.to_dict()
# create an instance of UserAuditResponse from a dict
user_audit_response_from_dict = UserAuditResponse.from_dict(user_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


