# InstanceRegionChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RegionChangeResponseData]**](RegionChangeResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.instance_region_change_response import InstanceRegionChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceRegionChangeResponse from a JSON string
instance_region_change_response_instance = InstanceRegionChangeResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceRegionChangeResponse.to_json())

# convert the object into a dict
instance_region_change_response_dict = instance_region_change_response_instance.to_dict()
# create an instance of InstanceRegionChangeResponse from a dict
instance_region_change_response_from_dict = InstanceRegionChangeResponse.from_dict(instance_region_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


