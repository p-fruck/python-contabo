# ListVipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ListVipResponseData]**](ListVipResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_vip_response import ListVipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListVipResponse from a JSON string
list_vip_response_instance = ListVipResponse.from_json(json)
# print the JSON string representation of the object
print(ListVipResponse.to_json())

# convert the object into a dict
list_vip_response_dict = list_vip_response_instance.to_dict()
# create an instance of ListVipResponse from a dict
list_vip_response_from_dict = ListVipResponse.from_dict(list_vip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


