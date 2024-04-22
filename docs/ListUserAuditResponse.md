# ListUserAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[UserAuditResponse]**](UserAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_user_audit_response import ListUserAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserAuditResponse from a JSON string
list_user_audit_response_instance = ListUserAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ListUserAuditResponse.to_json())

# convert the object into a dict
list_user_audit_response_dict = list_user_audit_response_instance.to_dict()
# create an instance of ListUserAuditResponse from a dict
list_user_audit_response_from_dict = ListUserAuditResponse.from_dict(list_user_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


