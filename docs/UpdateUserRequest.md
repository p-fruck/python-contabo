# UpdateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The name of the user. Names may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user. | [optional] 
**last_name** | **str** | The last name of the user. Users may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per user. | [optional] 
**email** | **str** | The email of the user to which activation and forgot password links are being sent to. There is a limit of 255 characters per email. | [optional] 
**enabled** | **bool** | If user is not enabled, he can&#39;t login and thus use services any longer. | [optional] 
**totp** | **bool** | Enable or disable two-factor authentication (2FA) via time based OTP. | [optional] 
**locale** | **str** | The locale of the user. This can be &#x60;de-DE&#x60;, &#x60;de&#x60;, &#x60;en-US&#x60;, &#x60;en&#x60; | [optional] 
**roles** | **List[int]** | The roles as list of &#x60;roleId&#x60;s of the user. | [optional] 

## Example

```python
from pfruck_contabo.models.update_user_request import UpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequest from a JSON string
update_user_request_instance = UpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequest.to_json())

# convert the object into a dict
update_user_request_dict = update_user_request_instance.to_dict()
# create an instance of UpdateUserRequest from a dict
update_user_request_from_dict = UpdateUserRequest.from_dict(update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


