# CreateInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | Initial contract period in months. Available periods are: 1, 3, 6 and 12 months. Default to 1 month | defaults to 1
**image_id** | **str** | ImageId to be used to setup the compute instance. Default is Ubuntu 22.04 | [optional]  if omitted the server will use the default value of "afecbb85-e2fc-46f0-9684-b46b1faf00bb"
**product_id** | **str** | Default is V45 | [optional]  if omitted the server will use the default value of "V45"
**region** | **str** | Instance Region where the compute instance should be located. Default is EU | [optional]  if omitted the server will use the default value of "EU"
**ssh_keys** | **[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into as &#x60;defaultUser&#x60; with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API. | [optional] 
**root_password** | **int** | &#x60;secretId&#x60; of the password for the &#x60;defaultUser&#x60; with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 
**license** | **str** | Additional licence in order to enhance your chosen product, mainly needed for software licenses on your product (not needed for windows). | [optional] 
**display_name** | **str** | The display name of the instance | [optional] 
**default_user** | **str** | Default user name created for login during (re-)installation with administrative privileges. Allowed values for Linux/BSD are &#x60;admin&#x60; (use sudo to apply administrative privileges like root) or &#x60;root&#x60;. Allowed values for Windows are &#x60;admin&#x60; (has administrative privileges like administrator) or &#x60;administrator&#x60;. | [optional]  if omitted the server will use the default value of "admin"
**add_ons** | [**CreateInstanceRequestAddOns**](CreateInstanceRequestAddOns.md) |  | [optional] 
**application_id** | **str** | Application ID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


