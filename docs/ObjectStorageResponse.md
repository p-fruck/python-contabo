# ObjectStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**object_storage_id** | **str** | Your object storage id | 
**created_date** | **datetime** | Creation date for object storage. | 
**cancel_date** | **date** | Cancellation date for object storage. | 
**auto_scaling** | [**AutoScalingTypeResponse**](AutoScalingTypeResponse.md) | Autoscaling settings | 
**data_center** | **str** | Data center your object storage is located | 
**total_purchased_space_tb** | **float** | Amount of purchased / requested object storage in TB. | 
**s3_url** | **str** | S3 URL to connect to your S3 compatible object storage | 
**s3_tenant_id** | **str** | Your S3 tenantId. Only required for public sharing. | 
**status** | **str** | The object storage status | 
**region** | **str** | The region where your object storage is located | 
**display_name** | **str** | Display name for object storage. | 

## Example

```python
from pfruck_contabo.models.object_storage_response import ObjectStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStorageResponse from a JSON string
object_storage_response_instance = ObjectStorageResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStorageResponse.to_json())

# convert the object into a dict
object_storage_response_dict = object_storage_response_instance.to_dict()
# create an instance of ObjectStorageResponse from a dict
object_storage_response_from_dict = ObjectStorageResponse.from_dict(object_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


