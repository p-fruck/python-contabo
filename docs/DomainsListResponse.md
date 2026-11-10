# DomainsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[DomainResponse]**](DomainResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.domains_list_response import DomainsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsListResponse from a JSON string
domains_list_response_instance = DomainsListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainsListResponse.to_json())

# convert the object into a dict
domains_list_response_dict = domains_list_response_instance.to_dict()
# create an instance of DomainsListResponse from a dict
domains_list_response_from_dict = DomainsListResponse.from_dict(domains_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


