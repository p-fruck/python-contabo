# RecordAuditResponseData


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
**record_id** | **int** | The identifier of the Zone recordd | 
**zone_name** | **str** | DNS Zone name | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.record_audit_response_data import RecordAuditResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAuditResponseData from a JSON string
record_audit_response_data_instance = RecordAuditResponseData.from_json(json)
# print the JSON string representation of the object
print(RecordAuditResponseData.to_json())

# convert the object into a dict
record_audit_response_data_dict = record_audit_response_data_instance.to_dict()
# create an instance of RecordAuditResponseData from a dict
record_audit_response_data_from_dict = RecordAuditResponseData.from_dict(record_audit_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


