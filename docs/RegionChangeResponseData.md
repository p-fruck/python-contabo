# RegionChangeResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**ticket_number** | **int** | Support ticket number created for the region change | 

## Example

```python
from pfruck_contabo.models.region_change_response_data import RegionChangeResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RegionChangeResponseData from a JSON string
region_change_response_data_instance = RegionChangeResponseData.from_json(json)
# print the JSON string representation of the object
print(RegionChangeResponseData.to_json())

# convert the object into a dict
region_change_response_data_dict = region_change_response_data_instance.to_dict()
# create an instance of RegionChangeResponseData from a dict
region_change_response_data_from_dict = RegionChangeResponseData.from_dict(region_change_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


