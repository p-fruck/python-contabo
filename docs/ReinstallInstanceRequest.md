# ReinstallInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | ImageId to be used to setup the compute instance. | 
**ssh_keys** | **List[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into as &#x60;defaultUser&#x60; with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API. | [optional] 
**root_password** | **int** | &#x60;secretId&#x60; of the password for the &#x60;defaultUser&#x60; with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 
**default_user** | **str** | Default user name created for login during (re-)installation with administrative privileges. Allowed values for Linux/BSD are &#x60;admin&#x60; (use sudo to apply administrative privileges like root) or &#x60;root&#x60;. Allowed values for Windows are &#x60;admin&#x60; (has administrative privileges like administrator) or &#x60;administrator&#x60;. | [optional] [default to 'admin']
**application_id** | **str** | Application ID | [optional] 

## Example

```python
from pfruck_contabo.models.reinstall_instance_request import ReinstallInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReinstallInstanceRequest from a JSON string
reinstall_instance_request_instance = ReinstallInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(ReinstallInstanceRequest.to_json())

# convert the object into a dict
reinstall_instance_request_dict = reinstall_instance_request_instance.to_dict()
# create an instance of ReinstallInstanceRequest from a dict
reinstall_instance_request_from_dict = ReinstallInstanceRequest.from_dict(reinstall_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


