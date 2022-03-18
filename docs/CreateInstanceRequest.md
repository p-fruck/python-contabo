# CreateInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | ImageId to be used to setup the compute instance. Default is Ubuntu 20.04 | defaults to "db1409d2-ed92-4f2f-978e-7b2fa4a1ec90"
**product_id** | **str** | Default is V1 | defaults to "V1"
**region** | **str** | Instance Region where the compute instance should be located. Default is EU | defaults to "EU"
**period** | **int** | Initial contract period in months. Available periods are: 1, 3, 6 and 12 months. Default to 1 month | defaults to 1
**ssh_keys** | **[int]** | Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API. | [optional] 
**root_password** | **int** | Password id for admin user with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 
**license** | **str** | Additional licence in order to enhance your chosen product, mainly needed for software licenses on your product (not needed for windows). | [optional] 
**display_name** | **str** | The display name of the instance | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


