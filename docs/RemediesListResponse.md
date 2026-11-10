# RemediesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[RemedyResponse]**](RemedyResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.remedies_list_response import RemediesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemediesListResponse from a JSON string
remedies_list_response_instance = RemediesListResponse.from_json(json)
# print the JSON string representation of the object
print(RemediesListResponse.to_json())

# convert the object into a dict
remedies_list_response_dict = remedies_list_response_instance.to_dict()
# create an instance of RemediesListResponse from a dict
remedies_list_response_from_dict = RemediesListResponse.from_dict(remedies_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


