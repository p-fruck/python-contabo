# UpgradeObjectStorageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**object_storage_id** | **str** | Object storage id | 
**created_date** | **str** | Creation date for object storage. | 
**data_center** | **str** | Data center of the object storage. | 
**auto_scaling** | [**AutoScalingTypeResponse**](AutoScalingTypeResponse.md) | The autoscaling limit of the object storage. | 
**s3_url** | **str** | S3 URL to connect to your S3 compatible object storage | 
**status** | **str** | The object storage status | 
**total_purchased_space_tb** | **float** | Total purchased object storage space in TB. | 
**region** | **str** | The region where your object storage is located | 
**display_name** | **str** | Display name for object storage. | 

## Example

```python
from pfruck_contabo.models.upgrade_object_storage_response_data import UpgradeObjectStorageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeObjectStorageResponseData from a JSON string
upgrade_object_storage_response_data_instance = UpgradeObjectStorageResponseData.from_json(json)
# print the JSON string representation of the object
print(UpgradeObjectStorageResponseData.to_json())

# convert the object into a dict
upgrade_object_storage_response_data_dict = upgrade_object_storage_response_data_instance.to_dict()
# create an instance of UpgradeObjectStorageResponseData from a dict
upgrade_object_storage_response_data_from_dict = UpgradeObjectStorageResponseData.from_dict(upgrade_object_storage_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


