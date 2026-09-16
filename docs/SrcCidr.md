# SrcCidr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **List[str]** | IPv4 addresses in CIDR notation or \&quot;AnyIPv4\&quot; to allow all IPv4 sources (translates to 0.0.0.0/0) | [optional] 
**ipv6** | **List[str]** | IPv6 addresses in CIDR notation or \&quot;AnyIPv6\&quot; to allow all IPv6 sources (translates to ::/0) | [optional] 

## Example

```python
from pfruck_contabo.models.src_cidr import SrcCidr

# TODO update the JSON string below
json = "{}"
# create an instance of SrcCidr from a JSON string
src_cidr_instance = SrcCidr.from_json(json)
# print the JSON string representation of the object
print(SrcCidr.to_json())

# convert the object into a dict
src_cidr_dict = src_cidr_instance.to_dict()
# create an instance of SrcCidr from a dict
src_cidr_from_dict = SrcCidr.from_dict(src_cidr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


