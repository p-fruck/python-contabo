# UpgradeObjectStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scaling** | [**UpgradeAutoScalingType**](UpgradeAutoScalingType.md) | New monthly object storage size limit for autoscaling if enabled. | [optional] 
**total_purchased_space_tb** | **float** | New total object storage limit. If this number is larger than before you will also be billed for the added storage space. No downgrade possible. | [optional] 

## Example

```python
from pfruck_contabo.models.upgrade_object_storage_request import UpgradeObjectStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeObjectStorageRequest from a JSON string
upgrade_object_storage_request_instance = UpgradeObjectStorageRequest.from_json(json)
# print the JSON string representation of the object
print(UpgradeObjectStorageRequest.to_json())

# convert the object into a dict
upgrade_object_storage_request_dict = upgrade_object_storage_request_instance.to_dict()
# create an instance of UpgradeObjectStorageRequest from a dict
upgrade_object_storage_request_from_dict = UpgradeObjectStorageRequest.from_dict(upgrade_object_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


