# DataCenterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the data center | 
**slug** | **str** | Slug of the data center | 
**capabilities** | **List[str]** |  | 
**s3_url** | **str** | S3 URL of the data center | 
**region_name** | **str** | Name of the region | 
**region_slug** | **str** | Slug of the region | 
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 

## Example

```python
from pfruck_contabo.models.data_center_response import DataCenterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataCenterResponse from a JSON string
data_center_response_instance = DataCenterResponse.from_json(json)
# print the JSON string representation of the object
print(DataCenterResponse.to_json())

# convert the object into a dict
data_center_response_dict = data_center_response_instance.to_dict()
# create an instance of DataCenterResponse from a dict
data_center_response_from_dict = DataCenterResponse.from_dict(data_center_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


