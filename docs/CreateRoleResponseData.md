# CreateRoleResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**role_id** | **int** | Role&#39;s id | 

## Example

```python
from pfruck_contabo.models.create_role_response_data import CreateRoleResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleResponseData from a JSON string
create_role_response_data_instance = CreateRoleResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateRoleResponseData.to_json())

# convert the object into a dict
create_role_response_data_dict = create_role_response_data_instance.to_dict()
# create an instance of CreateRoleResponseData from a dict
create_role_response_data_from_dict = CreateRoleResponseData.from_dict(create_role_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


