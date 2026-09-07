# DomainAuditResponseData


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
**domain** | **str** | The identifier of the domain | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.domain_audit_response_data import DomainAuditResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAuditResponseData from a JSON string
domain_audit_response_data_instance = DomainAuditResponseData.from_json(json)
# print the JSON string representation of the object
print(DomainAuditResponseData.to_json())

# convert the object into a dict
domain_audit_response_data_dict = domain_audit_response_data_instance.to_dict()
# create an instance of DomainAuditResponseData from a dict
domain_audit_response_data_from_dict = DomainAuditResponseData.from_dict(domain_audit_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


