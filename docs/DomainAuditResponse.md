# DomainAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[DomainAuditResponseData]**](DomainAuditResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_audit_response import DomainAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAuditResponse from a JSON string
domain_audit_response_instance = DomainAuditResponse.from_json(json)
# print the JSON string representation of the object
print(DomainAuditResponse.to_json())

# convert the object into a dict
domain_audit_response_dict = domain_audit_response_instance.to_dict()
# create an instance of DomainAuditResponse from a dict
domain_audit_response_from_dict = DomainAuditResponse.from_dict(domain_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


