# InstancesResetPasswordActionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_keys** | **List[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into as &#x60;defaultUser&#x60; with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API. | [optional] 
**root_password** | **int** | &#x60;secretId&#x60; of the password for the &#x60;defaultUser&#x60; with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 

## Example

```python
from pfruck_contabo.models.instances_reset_password_actions_request import InstancesResetPasswordActionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesResetPasswordActionsRequest from a JSON string
instances_reset_password_actions_request_instance = InstancesResetPasswordActionsRequest.from_json(json)
# print the JSON string representation of the object
print(InstancesResetPasswordActionsRequest.to_json())

# convert the object into a dict
instances_reset_password_actions_request_dict = instances_reset_password_actions_request_instance.to_dict()
# create an instance of InstancesResetPasswordActionsRequest from a dict
instances_reset_password_actions_request_from_dict = InstancesResetPasswordActionsRequest.from_dict(instances_reset_password_actions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


