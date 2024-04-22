# FindPrivateNetworkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrivateNetworkResponse]**](PrivateNetworkResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_private_network_response import FindPrivateNetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindPrivateNetworkResponse from a JSON string
find_private_network_response_instance = FindPrivateNetworkResponse.from_json(json)
# print the JSON string representation of the object
print(FindPrivateNetworkResponse.to_json())

# convert the object into a dict
find_private_network_response_dict = find_private_network_response_instance.to_dict()
# create an instance of FindPrivateNetworkResponse from a dict
find_private_network_response_from_dict = FindPrivateNetworkResponse.from_dict(find_private_network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


