# ListSecretAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[SecretAuditResponse]**](SecretAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_secret_audit_response import ListSecretAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSecretAuditResponse from a JSON string
list_secret_audit_response_instance = ListSecretAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ListSecretAuditResponse.to_json())

# convert the object into a dict
list_secret_audit_response_dict = list_secret_audit_response_instance.to_dict()
# create an instance of ListSecretAuditResponse from a dict
list_secret_audit_response_from_dict = ListSecretAuditResponse.from_dict(list_secret_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


