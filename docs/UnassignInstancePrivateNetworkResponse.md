# UnassignInstancePrivateNetworkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InstanceAssignmentSelfLinks**](InstanceAssignmentSelfLinks.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.unassign_instance_private_network_response import UnassignInstancePrivateNetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignInstancePrivateNetworkResponse from a JSON string
unassign_instance_private_network_response_instance = UnassignInstancePrivateNetworkResponse.from_json(json)
# print the JSON string representation of the object
print(UnassignInstancePrivateNetworkResponse.to_json())

# convert the object into a dict
unassign_instance_private_network_response_dict = unassign_instance_private_network_response_instance.to_dict()
# create an instance of UnassignInstancePrivateNetworkResponse from a dict
unassign_instance_private_network_response_from_dict = UnassignInstancePrivateNetworkResponse.from_dict(unassign_instance_private_network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


