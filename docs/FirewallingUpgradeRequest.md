# FirewallingUpgradeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assign_firewalls** | **List[str]** | List of IDs of firewalls the upgraded instance should be assigned to immediately.   If the list is empty or this property is not provided the instance will be assigned to   your current default firewall. | [optional] 

## Example

```python
from pfruck_contabo.models.firewalling_upgrade_request import FirewallingUpgradeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallingUpgradeRequest from a JSON string
firewalling_upgrade_request_instance = FirewallingUpgradeRequest.from_json(json)
# print the JSON string representation of the object
print(FirewallingUpgradeRequest.to_json())

# convert the object into a dict
firewalling_upgrade_request_dict = firewalling_upgrade_request_instance.to_dict()
# create an instance of FirewallingUpgradeRequest from a dict
firewalling_upgrade_request_from_dict = FirewallingUpgradeRequest.from_dict(firewalling_upgrade_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


