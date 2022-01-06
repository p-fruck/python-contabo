# CreateInstanceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | ImageId to be used to setup the compute instance. Default is Ubuntu 20.04 | [default to 'db1409d2-ed92-4f2f-978e-7b2fa4a1ec90']
**product_id** | **str** | You can find &#x60;productId&#x60;s [here](https://contabo.com/en/product-list/?show_ids&#x3D;true). Default is V1 | [default to 'V1']
**region** | **str** | Instance Region where the compute instance should be located. Default is EU | [default to 'EU']
**ssh_keys** | **list[int]** | Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API. | [optional] 
**root_password** | **int** | Password id for admin user with administrator/root privileges. For Linux/BSD please use SSH, for Windows RDP. Please refer to Secrets Management API. | [optional] 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | [optional] 
**license** | **str** | Additional licence in order to enhance your chosen product, mainly needed for software licenses on your product (not needed for windows). | [optional] 
**period** | **int** | Initial contract period in months. Available periods are: 1, 3, 6 and 12 months. Default to 1 month | [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

