# PatchObjectStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name helps to differentiate between object storages, especially if they are in the same region. | 

## Example

```python
from pfruck_contabo.models.patch_object_storage_request import PatchObjectStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchObjectStorageRequest from a JSON string
patch_object_storage_request_instance = PatchObjectStorageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchObjectStorageRequest.to_json())

# convert the object into a dict
patch_object_storage_request_dict = patch_object_storage_request_instance.to_dict()
# create an instance of PatchObjectStorageRequest from a dict
patch_object_storage_request_from_dict = PatchObjectStorageRequest.from_dict(patch_object_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


