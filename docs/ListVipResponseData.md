# ListVipResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant Id. | 
**customer_id** | **str** | Customer&#39;s Id. | 
**vip_id** | **str** | Vip uuid. | 
**data_center** | **str** | data center. | 
**region** | **str** | Region | 
**resource_id** | **str** | Resource Id. | 
**resource_type** | **str** | The resourceType using the VIP. | [optional] 
**resource_name** | **str** | Resource name. | 
**resource_display_name** | **str** | Resource display name. | 
**ip_version** | **str** | Version of Ip. | 
**type** | **str** | The VIP type. | [optional] 
**v4** | [**IpV41**](IpV41.md) |  | [optional] 

## Example

```python
from pfruck_contabo.models.list_vip_response_data import ListVipResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListVipResponseData from a JSON string
list_vip_response_data_instance = ListVipResponseData.from_json(json)
# print the JSON string representation of the object
print(ListVipResponseData.to_json())

# convert the object into a dict
list_vip_response_data_dict = list_vip_response_data_instance.to_dict()
# create an instance of ListVipResponseData from a dict
list_vip_response_data_from_dict = ListVipResponseData.from_dict(list_vip_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


