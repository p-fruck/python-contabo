# InstanceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | Instance id which is assigned to firewall | 
**display_name** | **str** | Instance display name | 
**name** | **str** | Instance name | 
**product_id** | **str** | Product id | 
**ip_config** | [**IpConfig1**](IpConfig1.md) |  | 
**region_slug** | **str** | Slug of the region where the instance is located. | 
**region_name** | **str** | Name of the region where the instance is located. | 
**data_center_slug** | **str** | Slug of the data center where the instance is located. | 
**data_center_name** | **str** | Name of the data center where the instance is located. | 

## Example

```python
from pfruck_contabo.models.instance_details import InstanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceDetails from a JSON string
instance_details_instance = InstanceDetails.from_json(json)
# print the JSON string representation of the object
print(InstanceDetails.to_json())

# convert the object into a dict
instance_details_dict = instance_details_instance.to_dict()
# create an instance of InstanceDetails from a dict
instance_details_from_dict = InstanceDetails.from_dict(instance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


