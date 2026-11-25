# UserSwitchAccountDefaultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Default flag for the selected account | 

## Example

```python
from pfruck_contabo.models.user_switch_account_default_request import UserSwitchAccountDefaultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSwitchAccountDefaultRequest from a JSON string
user_switch_account_default_request_instance = UserSwitchAccountDefaultRequest.from_json(json)
# print the JSON string representation of the object
print(UserSwitchAccountDefaultRequest.to_json())

# convert the object into a dict
user_switch_account_default_request_dict = user_switch_account_default_request_instance.to_dict()
# create an instance of UserSwitchAccountDefaultRequest from a dict
user_switch_account_default_request_from_dict = UserSwitchAccountDefaultRequest.from_dict(user_switch_account_default_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


