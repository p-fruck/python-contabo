# UserSwitchAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**user_id** | **str** | The identifier of the sub user account. | 
**first_name** | **str** | The first name of the main account. | 
**last_name** | **str** | The last name of the main account. | 
**email** | **str** | The email of the main account | 
**totp** | **bool** | Enable or disable two-factor authentication (2FA) via time based OTP. | 
**default** | **bool** | Flag to mark if the account is set as default | 
**locale** | **str** | The locale of the user. This can be &#x60;de-DE&#x60;, &#x60;de&#x60;, &#x60;en-US&#x60;, &#x60;en&#x60; | 
**role_name** | **str** | The name of the role. | 
**owner** | **bool** | If user is owner he will have permissions to all API endpoints and resources. | 
**account_details** | [**AccountDetails**](AccountDetails.md) | Details about the primary account holder for this sub account. | 

## Example

```python
from pfruck_contabo.models.user_switch_account import UserSwitchAccount

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchAccount from a JSON string
user_switch_account_instance = UserSwitchAccount.from_json(json)
# print the JSON string representation of the object
print(UserSwitchAccount.to_json())

# convert the object into a dict
user_switch_account_dict = user_switch_account_instance.to_dict()
# create an instance of UserSwitchAccount from a dict
user_switch_account_from_dict = UserSwitchAccount.from_dict(user_switch_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


