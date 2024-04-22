# InstanceStopActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceStopActionResponseData]**](InstanceStopActionResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.instance_stop_action_response import InstanceStopActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStopActionResponse from a JSON string
instance_stop_action_response_instance = InstanceStopActionResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceStopActionResponse.to_json())

# convert the object into a dict
instance_stop_action_response_dict = instance_stop_action_response_instance.to_dict()
# create an instance of InstanceStopActionResponse from a dict
instance_stop_action_response_from_dict = InstanceStopActionResponse.from_dict(instance_stop_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


