# SecretAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The identifier of the audit entry. | 
**secret_id** | **float** | Secret&#39;s id | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**tenant_id** | **str** | Customer tenant id | 
**customer_id** | **str** | Customer number | 
**changed_by** | **str** | User ID | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.secret_audit_response import SecretAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretAuditResponse from a JSON string
secret_audit_response_instance = SecretAuditResponse.from_json(json)
# print the JSON string representation of the object
print(SecretAuditResponse.to_json())

# convert the object into a dict
secret_audit_response_dict = secret_audit_response_instance.to_dict()
# create an instance of SecretAuditResponse from a dict
secret_audit_response_from_dict = SecretAuditResponse.from_dict(secret_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


