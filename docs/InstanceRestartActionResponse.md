# InstanceRestartActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceRestartActionResponseData]**](InstanceRestartActionResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.instance_restart_action_response import InstanceRestartActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceRestartActionResponse from a JSON string
instance_restart_action_response_instance = InstanceRestartActionResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceRestartActionResponse.to_json())

# convert the object into a dict
instance_restart_action_response_dict = instance_restart_action_response_instance.to_dict()
# create an instance of InstanceRestartActionResponse from a dict
instance_restart_action_response_from_dict = InstanceRestartActionResponse.from_dict(instance_restart_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


