# ListObjectStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ObjectStorageResponse]**](ObjectStorageResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_object_storage_response import ListObjectStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectStorageResponse from a JSON string
list_object_storage_response_instance = ListObjectStorageResponse.from_json(json)
# print the JSON string representation of the object
print(ListObjectStorageResponse.to_json())

# convert the object into a dict
list_object_storage_response_dict = list_object_storage_response_instance.to_dict()
# create an instance of ListObjectStorageResponse from a dict
list_object_storage_response_from_dict = ListObjectStorageResponse.from_dict(list_object_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


