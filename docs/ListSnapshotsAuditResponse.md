# ListSnapshotsAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[SnapshotsAuditResponse]**](SnapshotsAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_snapshots_audit_response import ListSnapshotsAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotsAuditResponse from a JSON string
list_snapshots_audit_response_instance = ListSnapshotsAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotsAuditResponse.to_json())

# convert the object into a dict
list_snapshots_audit_response_dict = list_snapshots_audit_response_instance.to_dict()
# create an instance of ListSnapshotsAuditResponse from a dict
list_snapshots_audit_response_from_dict = ListSnapshotsAuditResponse.from_dict(list_snapshots_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


