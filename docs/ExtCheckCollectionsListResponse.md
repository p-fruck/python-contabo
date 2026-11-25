# ExtCheckCollectionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ExtCheckCollectionResponse]**](ExtCheckCollectionResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.ext_check_collections_list_response import ExtCheckCollectionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtCheckCollectionsListResponse from a JSON string
ext_check_collections_list_response_instance = ExtCheckCollectionsListResponse.from_json(json)
# print the JSON string representation of the object
print(ExtCheckCollectionsListResponse.to_json())

# convert the object into a dict
ext_check_collections_list_response_dict = ext_check_collections_list_response_instance.to_dict()
# create an instance of ExtCheckCollectionsListResponse from a dict
ext_check_collections_list_response_from_dict = ExtCheckCollectionsListResponse.from_dict(ext_check_collections_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


