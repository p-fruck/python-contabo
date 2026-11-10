# ChecksAuditListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ChecksAuditResponse]**](ChecksAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.checks_audit_list_response import ChecksAuditListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksAuditListResponse from a JSON string
checks_audit_list_response_instance = ChecksAuditListResponse.from_json(json)
# print the JSON string representation of the object
print(ChecksAuditListResponse.to_json())

# convert the object into a dict
checks_audit_list_response_dict = checks_audit_list_response_instance.to_dict()
# create an instance of ChecksAuditListResponse from a dict
checks_audit_list_response_from_dict = ChecksAuditListResponse.from_dict(checks_audit_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


