# CreatePrivateNetworkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | Region where the Private Network should be located. Default is &#x60;EU&#x60; | [optional] [default to 'EU']
**name** | **str** | The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per Private Network name. | 
**description** | **str** | The description of the Private Network. There is a limit of 255 characters per Private Network description. | [optional] 

## Example

```python
from pfruck_contabo.models.create_private_network_request import CreatePrivateNetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrivateNetworkRequest from a JSON string
create_private_network_request_instance = CreatePrivateNetworkRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePrivateNetworkRequest.to_json())

# convert the object into a dict
create_private_network_request_dict = create_private_network_request_instance.to_dict()
# create an instance of CreatePrivateNetworkRequest from a dict
create_private_network_request_from_dict = CreatePrivateNetworkRequest.from_dict(create_private_network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


