# IpV43


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP Address | 
**netmask_cidr** | **int** | Netmask CIDR | 
**gateway** | **str** | Gateway | 

## Example

```python
from pfruck_contabo.models.ip_v43 import IpV43

# TODO update the JSON string below
json = "{}"
# create an instance of IpV43 from a JSON string
ip_v43_instance = IpV43.from_json(json)
# print the JSON string representation of the object
print(IpV43.to_json())

# convert the object into a dict
ip_v43_dict = ip_v43_instance.to_dict()
# create an instance of IpV43 from a dict
ip_v43_from_dict = IpV43.from_dict(ip_v43_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


