# IpConfig2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v4** | [**IpV43**](IpV43.md) |  | 
**v6** | [**IpV6**](IpV6.md) |  | 

## Example

```python
from pfruck_contabo.models.ip_config2 import IpConfig2

# TODO update the JSON string below
json = "{}"
# create an instance of IpConfig2 from a JSON string
ip_config2_instance = IpConfig2.from_json(json)
# print the JSON string representation of the object
print(IpConfig2.to_json())

# convert the object into a dict
ip_config2_dict = ip_config2_instance.to_dict()
# create an instance of IpConfig2 from a dict
ip_config2_from_dict = IpConfig2.from_dict(ip_config2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


