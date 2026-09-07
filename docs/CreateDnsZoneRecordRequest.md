# CreateDnsZoneRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name, if empty the zone name will be used | [optional] 
**type** | **str** | DNS record type | 
**ttl** | **float** | TTL | 
**prio** | **float** | Prio | 
**data** | **str** | Data | 
**port** | **float** | Port | [optional] 
**weight** | **float** | Weight | [optional] 
**flag** | **float** | Flag | [optional] 
**tag** | **str** | Tag | [optional] 

## Example

```python
from pfruck_contabo.models.create_dns_zone_record_request import CreateDnsZoneRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDnsZoneRecordRequest from a JSON string
create_dns_zone_record_request_instance = CreateDnsZoneRecordRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDnsZoneRecordRequest.to_json())

# convert the object into a dict
create_dns_zone_record_request_dict = create_dns_zone_record_request_instance.to_dict()
# create an instance of CreateDnsZoneRecordRequest from a dict
create_dns_zone_record_request_from_dict = CreateDnsZoneRecordRequest.from_dict(create_dns_zone_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


