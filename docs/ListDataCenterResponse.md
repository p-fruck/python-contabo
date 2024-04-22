# ListDataCenterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[DataCenterResponse]**](DataCenterResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_data_center_response import ListDataCenterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDataCenterResponse from a JSON string
list_data_center_response_instance = ListDataCenterResponse.from_json(json)
# print the JSON string representation of the object
print(ListDataCenterResponse.to_json())

# convert the object into a dict
list_data_center_response_dict = list_data_center_response_instance.to_dict()
# create an instance of ListDataCenterResponse from a dict
list_data_center_response_from_dict = ListDataCenterResponse.from_dict(list_data_center_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


