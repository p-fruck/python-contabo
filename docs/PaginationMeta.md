# PaginationMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **float** | Number of elements per page. | 
**total_elements** | **float** | Number of overall matched elements. | 
**total_pages** | **float** | Overall number of pages. | 
**page** | **float** | Current number of page. | 

## Example

```python
from pfruck_contabo.models.pagination_meta import PaginationMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationMeta from a JSON string
pagination_meta_instance = PaginationMeta.from_json(json)
# print the JSON string representation of the object
print(PaginationMeta.to_json())

# convert the object into a dict
pagination_meta_dict = pagination_meta_instance.to_dict()
# create an instance of PaginationMeta from a dict
pagination_meta_from_dict = PaginationMeta.from_dict(pagination_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


