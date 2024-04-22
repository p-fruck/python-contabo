# ListImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ListImageResponseData]**](ListImageResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_image_response import ListImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListImageResponse from a JSON string
list_image_response_instance = ListImageResponse.from_json(json)
# print the JSON string representation of the object
print(ListImageResponse.to_json())

# convert the object into a dict
list_image_response_dict = list_image_response_instance.to_dict()
# create an instance of ListImageResponse from a dict
list_image_response_from_dict = ListImageResponse.from_dict(list_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


