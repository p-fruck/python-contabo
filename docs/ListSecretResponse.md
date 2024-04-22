# ListSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[SecretResponse]**](SecretResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.list_secret_response import ListSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSecretResponse from a JSON string
list_secret_response_instance = ListSecretResponse.from_json(json)
# print the JSON string representation of the object
print(ListSecretResponse.to_json())

# convert the object into a dict
list_secret_response_dict = list_secret_response_instance.to_dict()
# create an instance of ListSecretResponse from a dict
list_secret_response_from_dict = ListSecretResponse.from_dict(list_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


