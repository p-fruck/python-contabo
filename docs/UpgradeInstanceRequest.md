# UpgradeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_networking** | **object** | Set this attribute if you want to upgrade your instance with the Private Networking addon. Please provide an empty object for the time being as value. There will be more configuration possible in the future. | [optional] 

## Example

```python
from pfruck_contabo.models.upgrade_instance_request import UpgradeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeInstanceRequest from a JSON string
upgrade_instance_request_instance = UpgradeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(UpgradeInstanceRequest.to_json())

# convert the object into a dict
upgrade_instance_request_dict = upgrade_instance_request_instance.to_dict()
# create an instance of UpgradeInstanceRequest from a dict
upgrade_instance_request_from_dict = UpgradeInstanceRequest.from_dict(upgrade_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


