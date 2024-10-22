# AdditionalIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v4** | [**IpV42**](IpV42.md) |  | 

## Example

```python
from pfruck_contabo.models.additional_ip import AdditionalIp

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalIp from a JSON string
additional_ip_instance = AdditionalIp.from_json(json)
# print the JSON string representation of the object
print(AdditionalIp.to_json())

# convert the object into a dict
additional_ip_dict = additional_ip_instance.to_dict()
# create an instance of AdditionalIp from a dict
additional_ip_from_dict = AdditionalIp.from_dict(additional_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


