# TagAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**id** | **float** | The identifier of the audit entry. | 
**tag_id** | **int** | The identifier of the audit entry. | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**changed_by** | **str** | User ID | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.tag_audit_response import TagAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagAuditResponse from a JSON string
tag_audit_response_instance = TagAuditResponse.from_json(json)
# print the JSON string representation of the object
print(TagAuditResponse.to_json())

# convert the object into a dict
tag_audit_response_dict = tag_audit_response_instance.to_dict()
# create an instance of TagAuditResponse from a dict
tag_audit_response_from_dict = TagAuditResponse.from_dict(tag_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


