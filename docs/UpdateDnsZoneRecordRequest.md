# UpdateDnsZoneRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **float** | TTL | 
**prio** | **float** | Prio | 
**type** | **str** | DNS record type | 
**data** | **str** | Data | 
**port** | **float** | Port | [optional] 
**weight** | **float** | Weight | [optional] 
**flag** | **float** | Flag | [optional] 
**tag** | **str** | Tag | [optional] 

## Example

```python
from pfruck_contabo.models.update_dns_zone_record_request import UpdateDnsZoneRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDnsZoneRecordRequest from a JSON string
update_dns_zone_record_request_instance = UpdateDnsZoneRecordRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDnsZoneRecordRequest.to_json())

# convert the object into a dict
update_dns_zone_record_request_dict = update_dns_zone_record_request_instance.to_dict()
# create an instance of UpdateDnsZoneRecordRequest from a dict
update_dns_zone_record_request_from_dict = UpdateDnsZoneRecordRequest.from_dict(update_dns_zone_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


