# InstanceResetPasswordActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceResetPasswordActionResponseData]**](InstanceResetPasswordActionResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.instance_reset_password_action_response import InstanceResetPasswordActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceResetPasswordActionResponse from a JSON string
instance_reset_password_action_response_instance = InstanceResetPasswordActionResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceResetPasswordActionResponse.to_json())

# convert the object into a dict
instance_reset_password_action_response_dict = instance_reset_password_action_response_instance.to_dict()
# create an instance of InstanceResetPasswordActionResponse from a dict
instance_reset_password_action_response_from_dict = InstanceResetPasswordActionResponse.from_dict(instance_reset_password_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


