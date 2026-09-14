# DnsZoneRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**record_id** | **float** | RecordId | 
**name** | **str** | Name, if empty the zone name will be used | 
**type** | **str** | Type | 
**ttl** | **float** | TTL | 
**prio** | **float** | Prio | 
**data** | **str** | Data | 
**port** | **float** | Port | 
**weight** | **float** | Weight | 
**flag** | **float** | Flag | 
**tag** | **str** | Tag | 

## Example

```python
from pfruck_contabo.models.dns_zone_record_response import DnsZoneRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnsZoneRecordResponse from a JSON string
dns_zone_record_response_instance = DnsZoneRecordResponse.from_json(json)
# print the JSON string representation of the object
print(DnsZoneRecordResponse.to_json())

# convert the object into a dict
dns_zone_record_response_dict = dns_zone_record_response_instance.to_dict()
# create an instance of DnsZoneRecordResponse from a dict
dns_zone_record_response_from_dict = DnsZoneRecordResponse.from_dict(dns_zone_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


