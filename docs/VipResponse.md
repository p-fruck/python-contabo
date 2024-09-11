# VipResponse


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
from pfruck_contabo.models.vip_response import VipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VipResponse from a JSON string
vip_response_instance = VipResponse.from_json(json)
# print the JSON string representation of the object
print(VipResponse.to_json())

# convert the object into a dict
vip_response_dict = vip_response_instance.to_dict()
# create an instance of VipResponse from a dict
vip_response_from_dict = VipResponse.from_dict(vip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


