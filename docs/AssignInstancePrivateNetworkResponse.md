# AssignInstancePrivateNetworkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**InstanceAssignmentSelfLinks**](InstanceAssignmentSelfLinks.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.assign_instance_private_network_response import AssignInstancePrivateNetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignInstancePrivateNetworkResponse from a JSON string
assign_instance_private_network_response_instance = AssignInstancePrivateNetworkResponse.from_json(json)
# print the JSON string representation of the object
print(AssignInstancePrivateNetworkResponse.to_json())

# convert the object into a dict
assign_instance_private_network_response_dict = assign_instance_private_network_response_instance.to_dict()
# create an instance of AssignInstancePrivateNetworkResponse from a dict
assign_instance_private_network_response_from_dict = AssignInstancePrivateNetworkResponse.from_dict(assign_instance_private_network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


