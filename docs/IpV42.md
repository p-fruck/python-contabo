# IpV42


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP Address | 
**netmask_cidr** | **int** | Netmask CIDR | 
**gateway** | **str** | Gateway | 

## Example

```python
from pfruck_contabo.models.ip_v42 import IpV42

# TODO update the JSON string below
json = "{}"
# create an instance of IpV42 from a JSON string
ip_v42_instance = IpV42.from_json(json)
# print the JSON string representation of the object
print(IpV42.to_json())

# convert the object into a dict
ip_v42_dict = ip_v42_instance.to_dict()
# create an instance of IpV42 from a dict
ip_v42_from_dict = IpV42.from_dict(ip_v42_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


