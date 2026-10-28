# ChecksAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 
**audit_id** | **int** | The ID of the audit entry. | 
**action** | **str** | Type of the action. | 
**foreign_changed_by** | **str** | Id of a foreign user (given on the api request via header) who performed the change | 
**foreign_username** | **str** | Name of the foreign user (given on the api request via header) which led to the change. | 
**changed_by** | **str** | Id of user who performed the change | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**changes** | [**Changes**](Changes.md) | List of changed properties | 
**check_id** | **float** | Check&#39;s id | 

## Example

```python
from pfruck_contabo.models.checks_audit_response import ChecksAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksAuditResponse from a JSON string
checks_audit_response_instance = ChecksAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ChecksAuditResponse.to_json())

# convert the object into a dict
checks_audit_response_dict = checks_audit_response_instance.to_dict()
# create an instance of ChecksAuditResponse from a dict
checks_audit_response_from_dict = ChecksAuditResponse.from_dict(checks_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


