# ListRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[RoleResponse]**](RoleResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_role_response import ListRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoleResponse from a JSON string
list_role_response_instance = ListRoleResponse.from_json(json)
# print the JSON string representation of the object
print(ListRoleResponse.to_json())

# convert the object into a dict
list_role_response_dict = list_role_response_instance.to_dict()
# create an instance of ListRoleResponse from a dict
list_role_response_from_dict = ListRoleResponse.from_dict(list_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


