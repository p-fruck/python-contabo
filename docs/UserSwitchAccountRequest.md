# UserSwitchAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID | 
**tenant_id** | **str** | Tenant ID | 
**email** | **str** | Email of the user | 

## Example

```python
from pfruck_contabo.models.user_switch_account_request import UserSwitchAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchAccountRequest from a JSON string
user_switch_account_request_instance = UserSwitchAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UserSwitchAccountRequest.to_json())

# convert the object into a dict
user_switch_account_request_dict = user_switch_account_request_instance.to_dict()
# create an instance of UserSwitchAccountRequest from a dict
user_switch_account_request_from_dict = UserSwitchAccountRequest.from_dict(user_switch_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


