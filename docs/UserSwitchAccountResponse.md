# UserSwitchAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserSwitchAccountTokens]**](UserSwitchAccountTokens.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.user_switch_account_response import UserSwitchAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchAccountResponse from a JSON string
user_switch_account_response_instance = UserSwitchAccountResponse.from_json(json)
# print the JSON string representation of the object
print(UserSwitchAccountResponse.to_json())

# convert the object into a dict
user_switch_account_response_dict = user_switch_account_response_instance.to_dict()
# create an instance of UserSwitchAccountResponse from a dict
user_switch_account_response_from_dict = UserSwitchAccountResponse.from_dict(user_switch_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


