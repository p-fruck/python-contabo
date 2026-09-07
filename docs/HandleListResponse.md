# HandleListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[HandleResponse]**](HandleResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.handle_list_response import HandleListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandleListResponse from a JSON string
handle_list_response_instance = HandleListResponse.from_json(json)
# print the JSON string representation of the object
print(HandleListResponse.to_json())

# convert the object into a dict
handle_list_response_dict = handle_list_response_instance.to_dict()
# create an instance of HandleListResponse from a dict
handle_list_response_from_dict = HandleListResponse.from_dict(handle_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


