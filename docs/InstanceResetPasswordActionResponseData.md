# InstanceResetPasswordActionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | Compute instance / resource id | 
**action** | **str** | Action that was triggered | 

## Example

```python
from pfruck_contabo.models.instance_reset_password_action_response_data import InstanceResetPasswordActionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceResetPasswordActionResponseData from a JSON string
instance_reset_password_action_response_data_instance = InstanceResetPasswordActionResponseData.from_json(json)
# print the JSON string representation of the object
print(InstanceResetPasswordActionResponseData.to_json())

# convert the object into a dict
instance_reset_password_action_response_data_dict = instance_reset_password_action_response_data_instance.to_dict()
# create an instance of InstanceResetPasswordActionResponseData from a dict
instance_reset_password_action_response_data_from_dict = InstanceResetPasswordActionResponseData.from_dict(instance_reset_password_action_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


