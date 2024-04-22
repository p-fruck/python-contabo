# FindRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoleResponse]**](RoleResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_role_response import FindRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindRoleResponse from a JSON string
find_role_response_instance = FindRoleResponse.from_json(json)
# print the JSON string representation of the object
print(FindRoleResponse.to_json())

# convert the object into a dict
find_role_response_dict = find_role_response_instance.to_dict()
# create an instance of FindRoleResponse from a dict
find_role_response_from_dict = FindRoleResponse.from_dict(find_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


