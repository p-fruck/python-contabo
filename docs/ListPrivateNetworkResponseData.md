# ListPrivateNetworkResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**private_network_id** | **int** | Private Network&#39;s id | 
**data_center** | **str** | The data center where your Private Network is located | 
**region** | **str** | The slug of the region where your Private Network is located | 
**region_name** | **str** | The region where your Private Network is located | 
**name** | **str** | The name of the Private Network | 
**description** | **str** | The description of the Private Network | 
**cidr** | **str** | The cidr range of the Private Network | 
**available_ips** | **int** | The total available IPs of the Private Network | 
**created_date** | **datetime** | The creation date of the Private Network | 
**instances** | [**[Instances]**](Instances.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


