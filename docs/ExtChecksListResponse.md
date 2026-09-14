# ExtChecksListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ExtCheckResponse]**](ExtCheckResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.ext_checks_list_response import ExtChecksListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtChecksListResponse from a JSON string
ext_checks_list_response_instance = ExtChecksListResponse.from_json(json)
# print the JSON string representation of the object
print(ExtChecksListResponse.to_json())

# convert the object into a dict
ext_checks_list_response_dict = ext_checks_list_response_instance.to_dict()
# create an instance of ExtChecksListResponse from a dict
ext_checks_list_response_from_dict = ExtChecksListResponse.from_dict(ext_checks_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


