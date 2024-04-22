# ListRoleAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoleAuditResponse]**](RoleAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_role_audit_response import ListRoleAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoleAuditResponse from a JSON string
list_role_audit_response_instance = ListRoleAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ListRoleAuditResponse.to_json())

# convert the object into a dict
list_role_audit_response_dict = list_role_audit_response_instance.to_dict()
# create an instance of ListRoleAuditResponse from a dict
list_role_audit_response_from_dict = ListRoleAuditResponse.from_dict(list_role_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


