# ApiDnsZoneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DnsZoneResponse]**](DnsZoneResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.api_dns_zone_response import ApiDnsZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDnsZoneResponse from a JSON string
api_dns_zone_response_instance = ApiDnsZoneResponse.from_json(json)
# print the JSON string representation of the object
print(ApiDnsZoneResponse.to_json())

# convert the object into a dict
api_dns_zone_response_dict = api_dns_zone_response_instance.to_dict()
# create an instance of ApiDnsZoneResponse from a dict
api_dns_zone_response_from_dict = ApiDnsZoneResponse.from_dict(api_dns_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


