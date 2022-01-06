# ReinstallInstanceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | ImageId to be used to setup the compute instance. | 
**ssh_keys** | **list[int]** | Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API. | [optional] 
**root_password** | **int** | Password id for admin user with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

