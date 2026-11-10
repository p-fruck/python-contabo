# RecordAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[RecordAuditResponseData]**](RecordAuditResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.record_audit_response import RecordAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAuditResponse from a JSON string
record_audit_response_instance = RecordAuditResponse.from_json(json)
# print the JSON string representation of the object
print(RecordAuditResponse.to_json())

# convert the object into a dict
record_audit_response_dict = record_audit_response_instance.to_dict()
# create an instance of RecordAuditResponse from a dict
record_audit_response_from_dict = RecordAuditResponse.from_dict(record_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


