# AuditCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 
**count** | **float** | Audit for replay quantity | 

## Example

```python
from pfruck_contabo.models.audit_count_response import AuditCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCountResponse from a JSON string
audit_count_response_instance = AuditCountResponse.from_json(json)
# print the JSON string representation of the object
print(AuditCountResponse.to_json())

# convert the object into a dict
audit_count_response_dict = audit_count_response_instance.to_dict()
# create an instance of AuditCountResponse from a dict
audit_count_response_from_dict = AuditCountResponse.from_dict(audit_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


