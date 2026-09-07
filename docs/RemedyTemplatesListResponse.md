# RemedyTemplatesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[RemedyTemplateResponse]**](RemedyTemplateResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.remedy_templates_list_response import RemedyTemplatesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemedyTemplatesListResponse from a JSON string
remedy_templates_list_response_instance = RemedyTemplatesListResponse.from_json(json)
# print the JSON string representation of the object
print(RemedyTemplatesListResponse.to_json())

# convert the object into a dict
remedy_templates_list_response_dict = remedy_templates_list_response_instance.to_dict()
# create an instance of RemedyTemplatesListResponse from a dict
remedy_templates_list_response_from_dict = RemedyTemplatesListResponse.from_dict(remedy_templates_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


