# RegionChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | Target region identifier passed to CMS | 
**method** | **str** | Region change method as defined by CMS | 

## Example

```python
from pfruck_contabo.models.region_change_request import RegionChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegionChangeRequest from a JSON string
region_change_request_instance = RegionChangeRequest.from_json(json)
# print the JSON string representation of the object
print(RegionChangeRequest.to_json())

# convert the object into a dict
region_change_request_dict = region_change_request_instance.to_dict()
# create an instance of RegionChangeRequest from a dict
region_change_request_from_dict = RegionChangeRequest.from_dict(region_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


