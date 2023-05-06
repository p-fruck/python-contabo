# InstancesActionsRescueRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_password** | **int** | &#x60;secretId&#x60; of the password to login into rescue system for the &#x60;root&#x60; user. | [optional] 
**ssh_keys** | **[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into rescue system as &#x60;root&#x60; user. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


