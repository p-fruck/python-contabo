# RemediesAuditListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[RemediesAuditResponse]**](RemediesAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.remedies_audit_list_response import RemediesAuditListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemediesAuditListResponse from a JSON string
remedies_audit_list_response_instance = RemediesAuditListResponse.from_json(json)
# print the JSON string representation of the object
print(RemediesAuditListResponse.to_json())

# convert the object into a dict
remedies_audit_list_response_dict = remedies_audit_list_response_instance.to_dict()
# create an instance of RemediesAuditListResponse from a dict
remedies_audit_list_response_from_dict = RemediesAuditListResponse.from_dict(remedies_audit_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


