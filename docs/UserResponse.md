# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**user_id** | **str** | User&#x27;s id | 
**first_name** | **str** | The first name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user. | 
**last_name** | **str** | The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user. | 
**email** | **str** | The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email. | 
**email_verified** | **bool** | User email verification status. | 
**enabled** | **bool** | If uses is not enabled, he can&#x27;t login and thus use services any longer. | 
**totp** | **bool** | Enable or disable two-factor authentication (2FA) via time based OTP. | 
**admin** | **bool** | If user is admin he will have permissions to all API endpoints and resources. Enabling this will superseed all role definitions and &#x60;accessAllResources&#x60;. | 
**access_all_resources** | **bool** | Allow access to all resources. This will superseed all assigned roles of type &#x60;resourcePermission&#x60;. You&#x27;ll need to set it to &#x60;true&#x60; in case you are not assigning roles of type &#x60;resourcePermission&#x60; explicitly. | 
**locale** | **str** | The locale of the user. This can be &#x60;de-DE&#x60;, &#x60;de&#x60;, &#x60;en-US&#x60;, &#x60;en&#x60; | 
**roles** | [**list[RoleResponse]**](RoleResponse.md) | The roles as list of &#x60;roleId&#x60;s of the user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

