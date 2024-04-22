# UpgradeObjectStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | 
**data** | [**List[UpgradeObjectStorageResponseData]**](UpgradeObjectStorageResponseData.md) |  | 

## Example

```python
from pfruck_contabo.models.upgrade_object_storage_response import UpgradeObjectStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeObjectStorageResponse from a JSON string
upgrade_object_storage_response_instance = UpgradeObjectStorageResponse.from_json(json)
# print the JSON string representation of the object
print(UpgradeObjectStorageResponse.to_json())

# convert the object into a dict
upgrade_object_storage_response_dict = upgrade_object_storage_response_instance.to_dict()
# create an instance of UpgradeObjectStorageResponse from a dict
upgrade_object_storage_response_from_dict = UpgradeObjectStorageResponse.from_dict(upgrade_object_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


