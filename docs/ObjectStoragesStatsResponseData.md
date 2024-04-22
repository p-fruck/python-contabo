# ObjectStoragesStatsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**used_space_tb** | **float** | Currently used space in TB. | 
**used_space_percentage** | **float** | Currently used space in percentage. | 
**number_of_objects** | **int** | Number of all objects (i.e. files and folders) in object storage. | 

## Example

```python
from pfruck_contabo.models.object_storages_stats_response_data import ObjectStoragesStatsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStoragesStatsResponseData from a JSON string
object_storages_stats_response_data_instance = ObjectStoragesStatsResponseData.from_json(json)
# print the JSON string representation of the object
print(ObjectStoragesStatsResponseData.to_json())

# convert the object into a dict
object_storages_stats_response_data_dict = object_storages_stats_response_data_instance.to_dict()
# create an instance of ObjectStoragesStatsResponseData from a dict
object_storages_stats_response_data_from_dict = ObjectStoragesStatsResponseData.from_dict(object_storages_stats_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


