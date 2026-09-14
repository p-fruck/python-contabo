# UserSwitchAccountTokens


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**token** | **str** | Token | 
**refresh_token** | **str** | Refresh Token | 

## Example

```python
from pfruck_contabo.models.user_switch_account_tokens import UserSwitchAccountTokens

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchAccountTokens from a JSON string
user_switch_account_tokens_instance = UserSwitchAccountTokens.from_json(json)
# print the JSON string representation of the object
print(UserSwitchAccountTokens.to_json())

# convert the object into a dict
user_switch_account_tokens_dict = user_switch_account_tokens_instance.to_dict()
# create an instance of UserSwitchAccountTokens from a dict
user_switch_account_tokens_from_dict = UserSwitchAccountTokens.from_dict(user_switch_account_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


