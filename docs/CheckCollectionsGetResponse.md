# CheckCollectionsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CheckCollectionResponse]**](CheckCollectionResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.check_collections_get_response import CheckCollectionsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionsGetResponse from a JSON string
check_collections_get_response_instance = CheckCollectionsGetResponse.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionsGetResponse.to_json())

# convert the object into a dict
check_collections_get_response_dict = check_collections_get_response_instance.to_dict()
# create an instance of CheckCollectionsGetResponse from a dict
check_collections_get_response_from_dict = CheckCollectionsGetResponse.from_dict(check_collections_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


