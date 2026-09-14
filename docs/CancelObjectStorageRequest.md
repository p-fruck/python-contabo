# CancelObjectStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_date** | **datetime** | Date of cancellation | [optional] 

## Example

```python
from pfruck_contabo.models.cancel_object_storage_request import CancelObjectStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectStorageRequest from a JSON string
cancel_object_storage_request_instance = CancelObjectStorageRequest.from_json(json)
# print the JSON string representation of the object
print(CancelObjectStorageRequest.to_json())

# convert the object into a dict
cancel_object_storage_request_dict = cancel_object_storage_request_instance.to_dict()
# create an instance of CancelObjectStorageRequest from a dict
cancel_object_storage_request_from_dict = CancelObjectStorageRequest.from_dict(cancel_object_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


