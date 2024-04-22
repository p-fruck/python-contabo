# CancelObjectStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | 
**data** | [**List[CancelObjectStorageResponseData]**](CancelObjectStorageResponseData.md) |  | 

## Example

```python
from pfruck_contabo.models.cancel_object_storage_response import CancelObjectStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectStorageResponse from a JSON string
cancel_object_storage_response_instance = CancelObjectStorageResponse.from_json(json)
# print the JSON string representation of the object
print(CancelObjectStorageResponse.to_json())

# convert the object into a dict
cancel_object_storage_response_dict = cancel_object_storage_response_instance.to_dict()
# create an instance of CancelObjectStorageResponse from a dict
cancel_object_storage_response_from_dict = CancelObjectStorageResponse.from_dict(cancel_object_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


