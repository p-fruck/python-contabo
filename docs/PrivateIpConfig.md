# PrivateIpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v4** | [**List[IpV4]**](IpV4.md) |  | 

## Example

```python
from pfruck_contabo.models.private_ip_config import PrivateIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateIpConfig from a JSON string
private_ip_config_instance = PrivateIpConfig.from_json(json)
# print the JSON string representation of the object
print(PrivateIpConfig.to_json())

# convert the object into a dict
private_ip_config_dict = private_ip_config_instance.to_dict()
# create an instance of PrivateIpConfig from a dict
private_ip_config_from_dict = PrivateIpConfig.from_dict(private_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


