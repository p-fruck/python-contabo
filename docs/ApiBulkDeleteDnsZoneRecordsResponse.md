# ApiBulkDeleteDnsZoneRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BulkDeleteResultResponse]**](BulkDeleteResultResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.api_bulk_delete_dns_zone_records_response import ApiBulkDeleteDnsZoneRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBulkDeleteDnsZoneRecordsResponse from a JSON string
api_bulk_delete_dns_zone_records_response_instance = ApiBulkDeleteDnsZoneRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiBulkDeleteDnsZoneRecordsResponse.to_json())

# convert the object into a dict
api_bulk_delete_dns_zone_records_response_dict = api_bulk_delete_dns_zone_records_response_instance.to_dict()
# create an instance of ApiBulkDeleteDnsZoneRecordsResponse from a dict
api_bulk_delete_dns_zone_records_response_from_dict = ApiBulkDeleteDnsZoneRecordsResponse.from_dict(api_bulk_delete_dns_zone_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


