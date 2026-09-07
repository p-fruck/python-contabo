# IpConfig1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v4** | [**IpV42**](IpV42.md) |  | 
**v6** | [**IpV6**](IpV6.md) |  | 

## Example

```python
from pfruck_contabo.models.ip_config1 import IpConfig1

# TODO update the JSON string below
json = "{}"
# create an instance of IpConfig1 from a JSON string
ip_config1_instance = IpConfig1.from_json(json)
# print the JSON string representation of the object
print(IpConfig1.to_json())

# convert the object into a dict
ip_config1_dict = ip_config1_instance.to_dict()
# create an instance of IpConfig1 from a dict
ip_config1_from_dict = IpConfig1.from_dict(ip_config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


