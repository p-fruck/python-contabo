# CustomImagesStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomImagesStatsResponseData]**](CustomImagesStatsResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.custom_images_stats_response import CustomImagesStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImagesStatsResponse from a JSON string
custom_images_stats_response_instance = CustomImagesStatsResponse.from_json(json)
# print the JSON string representation of the object
print(CustomImagesStatsResponse.to_json())

# convert the object into a dict
custom_images_stats_response_dict = custom_images_stats_response_instance.to_dict()
# create an instance of CustomImagesStatsResponse from a dict
custom_images_stats_response_from_dict = CustomImagesStatsResponse.from_dict(custom_images_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


