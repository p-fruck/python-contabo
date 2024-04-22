# IpV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP Address | 
**netmask_cidr** | **int** | Netmask CIDR | 
**gateway** | **str** | Gateway | 

## Example

```python
from pfruck_contabo.models.ip_v4 import IpV4

# TODO update the JSON string below
json = "{}"
# create an instance of IpV4 from a JSON string
ip_v4_instance = IpV4.from_json(json)
# print the JSON string representation of the object
print(IpV4.to_json())

# convert the object into a dict
ip_v4_dict = ip_v4_instance.to_dict()
# create an instance of IpV4 from a dict
ip_v4_from_dict = IpV4.from_dict(ip_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


