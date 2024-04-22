# UserIsPasswordSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**is_password_set** | **bool** | Indicates if the user has set a password for his account | 

## Example

```python
from pfruck_contabo.models.user_is_password_set_response import UserIsPasswordSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserIsPasswordSetResponse from a JSON string
user_is_password_set_response_instance = UserIsPasswordSetResponse.from_json(json)
# print the JSON string representation of the object
print(UserIsPasswordSetResponse.to_json())

# convert the object into a dict
user_is_password_set_response_dict = user_is_password_set_response_instance.to_dict()
# create an instance of UserIsPasswordSetResponse from a dict
user_is_password_set_response_from_dict = UserIsPasswordSetResponse.from_dict(user_is_password_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


