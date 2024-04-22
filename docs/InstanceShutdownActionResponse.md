# InstanceShutdownActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceShutdownActionResponseData]**](InstanceShutdownActionResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.instance_shutdown_action_response import InstanceShutdownActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceShutdownActionResponse from a JSON string
instance_shutdown_action_response_instance = InstanceShutdownActionResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceShutdownActionResponse.to_json())

# convert the object into a dict
instance_shutdown_action_response_dict = instance_shutdown_action_response_instance.to_dict()
# create an instance of InstanceShutdownActionResponse from a dict
instance_shutdown_action_response_from_dict = InstanceShutdownActionResponse.from_dict(instance_shutdown_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


