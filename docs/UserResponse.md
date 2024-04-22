# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**user_id** | **str** | The identifier of the user. | 
**first_name** | **str** | The first name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user. | 
**last_name** | **str** | The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user. | 
**email** | **str** | The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email. | 
**email_verified** | **bool** | User email verification status. | 
**enabled** | **bool** | If uses is not enabled, he can&#39;t login and thus use services any longer. | 
**totp** | **bool** | Enable or disable two-factor authentication (2FA) via time based OTP. | 
**locale** | **str** | The locale of the user. This can be &#x60;de-DE&#x60;, &#x60;de&#x60;, &#x60;en-US&#x60;, &#x60;en&#x60; | 
**roles** | [**List[RoleResponse]**](RoleResponse.md) | The roles as list of &#x60;roleId&#x60;s of the user. | 
**owner** | **bool** | If user is owner he will have permissions to all API endpoints and resources. Enabling this will superseed all role definitions and &#x60;accessAllResources&#x60;. | 

## Example

```python
from pfruck_contabo.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


