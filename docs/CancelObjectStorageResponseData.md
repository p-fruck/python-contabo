# CancelObjectStorageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**object_storage_id** | **str** | Object Storage id | 
**cancel_date** | **date** | Cancellation date for object storage. | 
**display_name** | **str** | Display name for object storage. | 

## Example

```python
from pfruck_contabo.models.cancel_object_storage_response_data import CancelObjectStorageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectStorageResponseData from a JSON string
cancel_object_storage_response_data_instance = CancelObjectStorageResponseData.from_json(json)
# print the JSON string representation of the object
print(CancelObjectStorageResponseData.to_json())

# convert the object into a dict
cancel_object_storage_response_data_dict = cancel_object_storage_response_data_instance.to_dict()
# create an instance of CancelObjectStorageResponseData from a dict
cancel_object_storage_response_data_from_dict = CancelObjectStorageResponseData.from_dict(cancel_object_storage_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


