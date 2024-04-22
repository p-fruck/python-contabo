# IpV6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP Address | 
**netmask_cidr** | **int** | Netmask CIDR | 
**gateway** | **str** | Gateway | 

## Example

```python
from pfruck_contabo.models.ip_v6 import IpV6

# TODO update the JSON string below
json = "{}"
# create an instance of IpV6 from a JSON string
ip_v6_instance = IpV6.from_json(json)
# print the JSON string representation of the object
print(IpV6.to_json())

# convert the object into a dict
ip_v6_dict = ip_v6_instance.to_dict()
# create an instance of IpV6 from a dict
ip_v6_from_dict = IpV6.from_dict(ip_v6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


