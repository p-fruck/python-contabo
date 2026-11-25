# UserSwitchAccountDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserSwitchAccount]**](UserSwitchAccount.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.user_switch_account_default_response import UserSwitchAccountDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchAccountDefaultResponse from a JSON string
user_switch_account_default_response_instance = UserSwitchAccountDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(UserSwitchAccountDefaultResponse.to_json())

# convert the object into a dict
user_switch_account_default_response_dict = user_switch_account_default_response_instance.to_dict()
# create an instance of UserSwitchAccountDefaultResponse from a dict
user_switch_account_default_response_from_dict = UserSwitchAccountDefaultResponse.from_dict(user_switch_account_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


