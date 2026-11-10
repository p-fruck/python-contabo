# BulkDeleteDnsZoneRecordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_ids** | **List[int]** | List of zone record ids to delete | 

## Example

```python
from pfruck_contabo.models.bulk_delete_dns_zone_records_request import BulkDeleteDnsZoneRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteDnsZoneRecordsRequest from a JSON string
bulk_delete_dns_zone_records_request_instance = BulkDeleteDnsZoneRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteDnsZoneRecordsRequest.to_json())

# convert the object into a dict
bulk_delete_dns_zone_records_request_dict = bulk_delete_dns_zone_records_request_instance.to_dict()
# create an instance of BulkDeleteDnsZoneRecordsRequest from a dict
bulk_delete_dns_zone_records_request_from_dict = BulkDeleteDnsZoneRecordsRequest.from_dict(bulk_delete_dns_zone_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


