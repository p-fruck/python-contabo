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
**add_ons** | [**List[AddOnResponse]**](AddOnResponse.md) |  | 
**os_type** | **str** | Type of operating system (OS) | 
**status** | [**InstanceStatus**](InstanceStatus.md) |  | 
**ssh_keys** | **List[int]** | Array of &#x60;secretId&#x60;s of public SSH keys for logging into as &#x60;defaultUser&#x60; with administrator/root privileges. Applies to Linux/BSD systems. Please refer to Secrets Management API. | 

## Example

```python
from pfruck_contabo.models.create_instance_response_data import CreateInstanceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstanceResponseData from a JSON string
create_instance_response_data_instance = CreateInstanceResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateInstanceResponseData.to_json())

# convert the object into a dict
create_instance_response_data_dict = create_instance_response_data_instance.to_dict()
# create an instance of CreateInstanceResponseData from a dict
create_instance_response_data_from_dict = CreateInstanceResponseData.from_dict(create_instance_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


