# CreatePrivateNetworkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrivateNetworkResponse]**](PrivateNetworkResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_private_network_response import CreatePrivateNetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrivateNetworkResponse from a JSON string
create_private_network_response_instance = CreatePrivateNetworkResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePrivateNetworkResponse.to_json())

# convert the object into a dict
create_private_network_response_dict = create_private_network_response_instance.to_dict()
# create an instance of CreatePrivateNetworkResponse from a dict
create_private_network_response_from_dict = CreatePrivateNetworkResponse.from_dict(create_private_network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


