# ZoneAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ZoneAuditResponseData]**](ZoneAuditResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.zone_audit_response import ZoneAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneAuditResponse from a JSON string
zone_audit_response_instance = ZoneAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ZoneAuditResponse.to_json())

# convert the object into a dict
zone_audit_response_dict = zone_audit_response_instance.to_dict()
# create an instance of ZoneAuditResponse from a dict
zone_audit_response_from_dict = ZoneAuditResponse.from_dict(zone_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


