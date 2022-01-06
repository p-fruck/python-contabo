# ListInstancesResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Customer ID | 
**name** | **str** | Instance Name | 
**instance_id** | **int** | Instance ID | 
**region** | **str** | Instance Region where the compute instance should be located. | 
**product_id** | **str** | Product ID | 
**image_id** | **str** | Image&#x27;s id | 
**ip_config** | [**IpConfig**](IpConfig.md) |  | 
**mac_address** | **str** | MAC Address | 
**ram_mb** | **float** | Image RAM size in MB | 
**cpu_cores** | **int** | CPU core count | 
**os_type** | **str** | Type of operating system (OS) | 
**disk_mb** | **float** | Image Disk size in MB | 
**ssh_keys** | **list[str]** | Array of ids of public SSH Keys in order to access as admin user with root privileges (via sudo). Applies to Linux/BSD systems. Please refer to Secrets Management API. | 
**created_date** | **datetime** | The creation date for the instance | 
**cancel_date** | **date** | The date on which the instance will be cancelled | 
**status** | [**InstanceStatus**](InstanceStatus.md) |  | 
**v_host_id** | **int** | ID of host system | 
**add_ons** | [**list[AddOnResponse]**](AddOnResponse.md) |  | 
**error_message** | **str** | Message in case of an error. | [optional] 
**product_type** | **str** | Instance&#x27;s category depending on Product Id | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

