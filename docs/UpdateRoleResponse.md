# UpdateRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.update_role_response import UpdateRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleResponse from a JSON string
update_role_response_instance = UpdateRoleResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRoleResponse.to_json())

# convert the object into a dict
update_role_response_dict = update_role_response_instance.to_dict()
# create an instance of UpdateRoleResponse from a dict
update_role_response_from_dict = UpdateRoleResponse.from_dict(update_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


