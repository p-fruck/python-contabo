# CreateInstanceResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | Instance&#39;s id | 
**created_date** | **datetime** | Creation date for instance | 
**image_id** | **str** | Image&#39;s id | 
**product_id** | **str** | Product ID | 
**region** | **str** | Instance Region where the compute instance should be located. | 
**add_ons** | [**[AddOnResponse]**](AddOnResponse.md) |  | 
**os_type** | **str** | Type of operating system (OS) | 
**status** | [**InstanceStatus**](InstanceStatus.md) |  | 
**ssh_keys** | **[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into as &#x60;defaultUser&#x60; with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


