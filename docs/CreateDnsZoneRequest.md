# CreateDnsZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_name** | **str** | Zone name | 

## Example

```python
from pfruck_contabo.models.create_dns_zone_request import CreateDnsZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDnsZoneRequest from a JSON string
create_dns_zone_request_instance = CreateDnsZoneRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDnsZoneRequest.to_json())

# convert the object into a dict
create_dns_zone_request_dict = create_dns_zone_request_instance.to_dict()
# create an instance of CreateDnsZoneRequest from a dict
create_dns_zone_request_from_dict = CreateDnsZoneRequest.from_dict(create_dns_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


