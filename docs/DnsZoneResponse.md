# DnsZoneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**zone_name** | **str** | Zone name | 

## Example

```python
from pfruck_contabo.models.dns_zone_response import DnsZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnsZoneResponse from a JSON string
dns_zone_response_instance = DnsZoneResponse.from_json(json)
# print the JSON string representation of the object
print(DnsZoneResponse.to_json())

# convert the object into a dict
dns_zone_response_dict = dns_zone_response_instance.to_dict()
# create an instance of DnsZoneResponse from a dict
dns_zone_response_from_dict = DnsZoneResponse.from_dict(dns_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


