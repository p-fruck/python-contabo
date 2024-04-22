# ObjectStoragesStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ObjectStoragesStatsResponseData]**](ObjectStoragesStatsResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.object_storages_stats_response import ObjectStoragesStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStoragesStatsResponse from a JSON string
object_storages_stats_response_instance = ObjectStoragesStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectStoragesStatsResponse.to_json())

# convert the object into a dict
object_storages_stats_response_dict = object_storages_stats_response_instance.to_dict()
# create an instance of ObjectStoragesStatsResponse from a dict
object_storages_stats_response_from_dict = ObjectStoragesStatsResponse.from_dict(object_storages_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


