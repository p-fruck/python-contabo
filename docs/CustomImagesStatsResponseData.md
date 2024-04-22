# CustomImagesStatsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**current_images_count** | **float** | The number of existing custom images | 
**total_size_mb** | **float** | Total available disk space in MB | 
**used_size_mb** | **float** | Used disk space in MB | 
**free_size_mb** | **float** | Free disk space in MB | 

## Example

```python
from pfruck_contabo.models.custom_images_stats_response_data import CustomImagesStatsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImagesStatsResponseData from a JSON string
custom_images_stats_response_data_instance = CustomImagesStatsResponseData.from_json(json)
# print the JSON string representation of the object
print(CustomImagesStatsResponseData.to_json())

# convert the object into a dict
custom_images_stats_response_data_dict = custom_images_stats_response_data_instance.to_dict()
# create an instance of CustomImagesStatsResponseData from a dict
custom_images_stats_response_data_from_dict = CustomImagesStatsResponseData.from_dict(custom_images_stats_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


