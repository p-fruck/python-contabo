# IpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v4** | [**IpV4**](IpV4.md) |  | 
**v6** | [**IpV6**](IpV6.md) |  | 

## Example

```python
from pfruck_contabo.models.ip_config import IpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IpConfig from a JSON string
ip_config_instance = IpConfig.from_json(json)
# print the JSON string representation of the object
print(IpConfig.to_json())

# convert the object into a dict
ip_config_dict = ip_config_instance.to_dict()
# create an instance of IpConfig from a dict
ip_config_from_dict = IpConfig.from_dict(ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


