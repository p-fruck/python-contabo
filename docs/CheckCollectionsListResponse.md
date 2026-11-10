# CheckCollectionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[CheckCollectionResponse]**](CheckCollectionResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.check_collections_list_response import CheckCollectionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionsListResponse from a JSON string
check_collections_list_response_instance = CheckCollectionsListResponse.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionsListResponse.to_json())

# convert the object into a dict
check_collections_list_response_dict = check_collections_list_response_instance.to_dict()
# create an instance of CheckCollectionsListResponse from a dict
check_collections_list_response_from_dict = CheckCollectionsListResponse.from_dict(check_collections_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


