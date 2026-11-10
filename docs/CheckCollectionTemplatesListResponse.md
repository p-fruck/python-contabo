# CheckCollectionTemplatesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[CheckCollectionTemplateResponse]**](CheckCollectionTemplateResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.check_collection_templates_list_response import CheckCollectionTemplatesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionTemplatesListResponse from a JSON string
check_collection_templates_list_response_instance = CheckCollectionTemplatesListResponse.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionTemplatesListResponse.to_json())

# convert the object into a dict
check_collection_templates_list_response_dict = check_collection_templates_list_response_instance.to_dict()
# create an instance of CheckCollectionTemplatesListResponse from a dict
check_collection_templates_list_response_from_dict = CheckCollectionTemplatesListResponse.from_dict(check_collection_templates_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


