# CreateUserResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**user_id** | **str** | User&#39;s id | 

## Example

```python
from pfruck_contabo.models.create_user_response_data import CreateUserResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserResponseData from a JSON string
create_user_response_data_instance = CreateUserResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateUserResponseData.to_json())

# convert the object into a dict
create_user_response_data_dict = create_user_response_data_instance.to_dict()
# create an instance of CreateUserResponseData from a dict
create_user_response_data_from_dict = CreateUserResponseData.from_dict(create_user_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


