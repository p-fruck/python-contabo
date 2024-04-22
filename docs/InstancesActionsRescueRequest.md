# InstancesActionsRescueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_password** | **int** | &#x60;secretId&#x60; of the password to login into rescue system for the &#x60;root&#x60; user. | [optional] 
**ssh_keys** | **List[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into rescue system as &#x60;root&#x60; user. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 

## Example

```python
from pfruck_contabo.models.instances_actions_rescue_request import InstancesActionsRescueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesActionsRescueRequest from a JSON string
instances_actions_rescue_request_instance = InstancesActionsRescueRequest.from_json(json)
# print the JSON string representation of the object
print(InstancesActionsRescueRequest.to_json())

# convert the object into a dict
instances_actions_rescue_request_dict = instances_actions_rescue_request_instance.to_dict()
# create an instance of InstancesActionsRescueRequest from a dict
instances_actions_rescue_request_from_dict = InstancesActionsRescueRequest.from_dict(instances_actions_rescue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


