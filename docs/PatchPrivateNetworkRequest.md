# PatchPrivateNetworkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per Private Network. | [optional] 
**description** | **str** | The description of the Private Network. There is a limit of 255 characters per Private Network. | [optional] 

## Example

```python
from pfruck_contabo.models.patch_private_network_request import PatchPrivateNetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPrivateNetworkRequest from a JSON string
patch_private_network_request_instance = PatchPrivateNetworkRequest.from_json(json)
# print the JSON string representation of the object
print(PatchPrivateNetworkRequest.to_json())

# convert the object into a dict
patch_private_network_request_dict = patch_private_network_request_instance.to_dict()
# create an instance of PatchPrivateNetworkRequest from a dict
patch_private_network_request_from_dict = PatchPrivateNetworkRequest.from_dict(patch_private_network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


