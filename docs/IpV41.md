# IpV41


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address | 
**gateway** | **str** | Gateway | 
**netmask_cidr** | **int** | Netmask CIDR | 
**broadcast** | **str** | Broadcast address | 
**net** | **str** | Net address | 

## Example

```python
from pfruck_contabo.models.ip_v41 import IpV41

# TODO update the JSON string below
json = "{}"
# create an instance of IpV41 from a JSON string
ip_v41_instance = IpV41.from_json(json)
# print the JSON string representation of the object
print(IpV41.to_json())

# convert the object into a dict
ip_v41_dict = ip_v41_instance.to_dict()
# create an instance of IpV41 from a dict
ip_v41_from_dict = IpV41.from_dict(ip_v41_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


