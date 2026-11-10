# ExtCheckCollectionsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExtCheckCollectionResponse]**](ExtCheckCollectionResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.ext_check_collections_get_response import ExtCheckCollectionsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtCheckCollectionsGetResponse from a JSON string
ext_check_collections_get_response_instance = ExtCheckCollectionsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ExtCheckCollectionsGetResponse.to_json())

# convert the object into a dict
ext_check_collections_get_response_dict = ext_check_collections_get_response_instance.to_dict()
# create an instance of ExtCheckCollectionsGetResponse from a dict
ext_check_collections_get_response_from_dict = ExtCheckCollectionsGetResponse.from_dict(ext_check_collections_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


