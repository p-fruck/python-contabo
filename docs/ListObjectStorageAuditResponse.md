# ListObjectStorageAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ObjectStorageAuditResponse]**](ObjectStorageAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_object_storage_audit_response import ListObjectStorageAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectStorageAuditResponse from a JSON string
list_object_storage_audit_response_instance = ListObjectStorageAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ListObjectStorageAuditResponse.to_json())

# convert the object into a dict
list_object_storage_audit_response_dict = list_object_storage_audit_response_instance.to_dict()
# create an instance of ListObjectStorageAuditResponse from a dict
list_object_storage_audit_response_from_dict = ListObjectStorageAuditResponse.from_dict(list_object_storage_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


