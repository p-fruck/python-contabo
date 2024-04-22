# CreateRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateRoleResponseData]**](CreateRoleResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_role_response import CreateRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleResponse from a JSON string
create_role_response_instance = CreateRoleResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRoleResponse.to_json())

# convert the object into a dict
create_role_response_dict = create_role_response_instance.to_dict()
# create an instance of CreateRoleResponse from a dict
create_role_response_from_dict = CreateRoleResponse.from_dict(create_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


