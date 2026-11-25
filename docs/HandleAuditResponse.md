# HandleAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[HandleAuditResponseData]**](HandleAuditResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.handle_audit_response import HandleAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandleAuditResponse from a JSON string
handle_audit_response_instance = HandleAuditResponse.from_json(json)
# print the JSON string representation of the object
print(HandleAuditResponse.to_json())

# convert the object into a dict
handle_audit_response_dict = handle_audit_response_instance.to_dict()
# create an instance of HandleAuditResponse from a dict
handle_audit_response_from_dict = HandleAuditResponse.from_dict(handle_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


