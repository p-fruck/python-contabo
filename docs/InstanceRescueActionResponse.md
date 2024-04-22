# InstanceRescueActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceRescueActionResponseData]**](InstanceRescueActionResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.instance_rescue_action_response import InstanceRescueActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceRescueActionResponse from a JSON string
instance_rescue_action_response_instance = InstanceRescueActionResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceRescueActionResponse.to_json())

# convert the object into a dict
instance_rescue_action_response_dict = instance_rescue_action_response_instance.to_dict()
# create an instance of InstanceRescueActionResponse from a dict
instance_rescue_action_response_from_dict = InstanceRescueActionResponse.from_dict(instance_rescue_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


