# Nameserver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **List[str]** | Nameservers | 
**ip_v4** | **List[str]** | IPv4 of nameserver | [optional] 
**ip_v6** | **List[str]** | IPv6 of nameserver | [optional] 

## Example

```python
from pfruck_contabo.models.nameserver import Nameserver

# TODO update the JSON string below
json = "{}"
# create an instance of Nameserver from a JSON string
nameserver_instance = Nameserver.from_json(json)
# print the JSON string representation of the object
print(Nameserver.to_json())

# convert the object into a dict
nameserver_dict = nameserver_instance.to_dict()
# create an instance of Nameserver from a dict
nameserver_from_dict = Nameserver.from_dict(nameserver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


