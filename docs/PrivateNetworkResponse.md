# PrivateNetworkResponse


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
from pfruck_contabo.models.private_network_response import PrivateNetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkResponse from a JSON string
private_network_response_instance = PrivateNetworkResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkResponse.to_json())

# convert the object into a dict
private_network_response_dict = private_network_response_instance.to_dict()
# create an instance of PrivateNetworkResponse from a dict
private_network_response_from_dict = PrivateNetworkResponse.from_dict(private_network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


