# RoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Role&#39;s id | 
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**name** | **str** | Role&#39;s name | 
**admin** | **bool** | Admin | 
**access_all_resources** | **bool** | Access All Resources | 
**type** | **str** | Role type can be either &#x60;default&#x60; or &#x60;custom&#x60;. The &#x60;default&#x60; roles cannot be modified or deleted. | 
**permissions** | [**List[PermissionResponse]**](PermissionResponse.md) |  | [optional] 

## Example

```python
from pfruck_contabo.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print(RoleResponse.to_json())

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_from_dict = RoleResponse.from_dict(role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


