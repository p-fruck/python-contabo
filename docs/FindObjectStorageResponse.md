# FindObjectStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ObjectStorageResponse]**](ObjectStorageResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_object_storage_response import FindObjectStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindObjectStorageResponse from a JSON string
find_object_storage_response_instance = FindObjectStorageResponse.from_json(json)
# print the JSON string representation of the object
print(FindObjectStorageResponse.to_json())

# convert the object into a dict
find_object_storage_response_dict = find_object_storage_response_instance.to_dict()
# create an instance of FindObjectStorageResponse from a dict
find_object_storage_response_from_dict = FindObjectStorageResponse.from_dict(find_object_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


