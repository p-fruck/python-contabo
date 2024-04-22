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
**instances** | [**List[Instances]**](Instances.md) |  | 

## Example

```python
from pfruck_contabo.models.list_private_network_response_data import ListPrivateNetworkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListPrivateNetworkResponseData from a JSON string
list_private_network_response_data_instance = ListPrivateNetworkResponseData.from_json(json)
# print the JSON string representation of the object
print(ListPrivateNetworkResponseData.to_json())

# convert the object into a dict
list_private_network_response_data_dict = list_private_network_response_data_instance.to_dict()
# create an instance of ListPrivateNetworkResponseData from a dict
list_private_network_response_data_from_dict = ListPrivateNetworkResponseData.from_dict(list_private_network_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


