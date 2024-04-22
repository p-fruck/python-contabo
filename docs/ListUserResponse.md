# ListUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[UserResponse]**](UserResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_user_response import ListUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserResponse from a JSON string
list_user_response_instance = ListUserResponse.from_json(json)
# print the JSON string representation of the object
print(ListUserResponse.to_json())

# convert the object into a dict
list_user_response_dict = list_user_response_instance.to_dict()
# create an instance of ListUserResponse from a dict
list_user_response_from_dict = ListUserResponse.from_dict(list_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


