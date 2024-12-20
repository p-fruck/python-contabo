# ListInstancesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Customer ID | 
**additional_ips** | [**List[AdditionalIp]**](AdditionalIp.md) |  | 
**name** | **str** | Instance Name | 
**display_name** | **str** | Instance display name | 
**instance_id** | **int** | Instance ID | 
**data_center** | **str** | The data center where your Private Network is located | 
**region** | **str** | Instance region where the compute instance should be located. | 
**region_name** | **str** | The name of the region where the instance is located. | 
**product_id** | **str** | Product ID | 
**image_id** | **str** | Image&#39;s id | 
**ip_config** | [**IpConfig1**](IpConfig1.md) |  | 
**mac_address** | **str** | MAC Address | 
**ram_mb** | **float** | Image RAM size in MB | 
**cpu_cores** | **int** | CPU core count | 
**os_type** | **str** | Type of operating system (OS) | 
**disk_mb** | **float** | Image Disk size in MB | 
**ssh_keys** | **List[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into as &#x60;defaultUser&#x60; with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API. | 
**created_date** | **datetime** | The creation date for the instance | 
**cancel_date** | **date** | The date on which the instance will be cancelled | 
**status** | [**InstanceStatus**](InstanceStatus.md) |  | 
**v_host_id** | **int** | ID of host system | 
**v_host_number** | **int** | Number of host system | 
**v_host_name** | **str** | Name of host system | 
**add_ons** | [**List[AddOnResponse]**](AddOnResponse.md) |  | 
**error_message** | **str** | Message in case of an error. | [optional] 
**product_type** | **str** | Instance&#39;s category depending on Product Id | 
**product_name** | **str** | Instance&#39;s Product Name | 
**default_user** | **str** | Default user name created for login during (re-)installation with administrative privileges. Allowed values for Linux/BSD are &#x60;admin&#x60; (use sudo to apply administrative privileges like root) or &#x60;root&#x60;. Allowed values for Windows are &#x60;admin&#x60; (has administrative privileges like administrator) or &#x60;administrator&#x60;. | [optional] 

## Example

```python
from pfruck_contabo.models.list_instances_response_data import ListInstancesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListInstancesResponseData from a JSON string
list_instances_response_data_instance = ListInstancesResponseData.from_json(json)
# print the JSON string representation of the object
print(ListInstancesResponseData.to_json())

# convert the object into a dict
list_instances_response_data_dict = list_instances_response_data_instance.to_dict()
# create an instance of ListInstancesResponseData from a dict
list_instances_response_data_from_dict = ListInstancesResponseData.from_dict(list_instances_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


