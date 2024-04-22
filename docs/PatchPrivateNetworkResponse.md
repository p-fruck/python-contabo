# PatchPrivateNetworkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrivateNetworkResponse]**](PrivateNetworkResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.patch_private_network_response import PatchPrivateNetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPrivateNetworkResponse from a JSON string
patch_private_network_response_instance = PatchPrivateNetworkResponse.from_json(json)
# print the JSON string representation of the object
print(PatchPrivateNetworkResponse.to_json())

# convert the object into a dict
patch_private_network_response_dict = patch_private_network_response_instance.to_dict()
# create an instance of PatchPrivateNetworkResponse from a dict
patch_private_network_response_from_dict = PatchPrivateNetworkResponse.from_dict(patch_private_network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


