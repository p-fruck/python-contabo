# ListDnsZonesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[DnsZoneResponse]**](DnsZoneResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_dns_zones_response import ListDnsZonesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnsZonesResponse from a JSON string
list_dns_zones_response_instance = ListDnsZonesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDnsZonesResponse.to_json())

# convert the object into a dict
list_dns_zones_response_dict = list_dns_zones_response_instance.to_dict()
# create an instance of ListDnsZonesResponse from a dict
list_dns_zones_response_from_dict = ListDnsZonesResponse.from_dict(list_dns_zones_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


