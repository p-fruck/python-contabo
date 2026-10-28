# CheckTemplatesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[CheckTemplateResponse]**](CheckTemplateResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.check_templates_list_response import CheckTemplatesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTemplatesListResponse from a JSON string
check_templates_list_response_instance = CheckTemplatesListResponse.from_json(json)
# print the JSON string representation of the object
print(CheckTemplatesListResponse.to_json())

# convert the object into a dict
check_templates_list_response_dict = check_templates_list_response_instance.to_dict()
# create an instance of CheckTemplatesListResponse from a dict
check_templates_list_response_from_dict = CheckTemplatesListResponse.from_dict(check_templates_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


