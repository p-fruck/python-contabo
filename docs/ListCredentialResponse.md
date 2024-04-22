# ListCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[CredentialData]**](CredentialData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_credential_response import ListCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCredentialResponse from a JSON string
list_credential_response_instance = ListCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(ListCredentialResponse.to_json())

# convert the object into a dict
list_credential_response_dict = list_credential_response_instance.to_dict()
# create an instance of ListCredentialResponse from a dict
list_credential_response_from_dict = ListCredentialResponse.from_dict(list_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


