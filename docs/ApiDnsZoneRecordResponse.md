# ApiDnsZoneRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DnsZoneRecordResponse]**](DnsZoneRecordResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.api_dns_zone_record_response import ApiDnsZoneRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDnsZoneRecordResponse from a JSON string
api_dns_zone_record_response_instance = ApiDnsZoneRecordResponse.from_json(json)
# print the JSON string representation of the object
print(ApiDnsZoneRecordResponse.to_json())

# convert the object into a dict
api_dns_zone_record_response_dict = api_dns_zone_record_response_instance.to_dict()
# create an instance of ApiDnsZoneRecordResponse from a dict
api_dns_zone_record_response_from_dict = ApiDnsZoneRecordResponse.from_dict(api_dns_zone_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


