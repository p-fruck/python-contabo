# Instances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | Instance id | 
**display_name** | **str** | Instance display name | 
**name** | **str** | Instance name | 
**product_id** | **str** | Product id | 
**private_ip_config** | [**PrivateIpConfig**](PrivateIpConfig.md) |  | 
**ip_config** | [**IpConfig**](IpConfig.md) |  | 
**status** | **str** | State of the instance in the Private Network | 
**error_message** | **str** | Message in case of an error. | [optional] 

## Example

```python
from pfruck_contabo.models.instances import Instances

# TODO update the JSON string below
json = "{}"
# create an instance of Instances from a JSON string
instances_instance = Instances.from_json(json)
# print the JSON string representation of the object
print(Instances.to_json())

# convert the object into a dict
instances_dict = instances_instance.to_dict()
# create an instance of Instances from a dict
instances_from_dict = Instances.from_dict(instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


