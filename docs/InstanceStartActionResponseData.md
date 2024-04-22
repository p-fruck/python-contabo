# InstanceStartActionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | Compute instance / resource id | 
**action** | **str** | Action that was triggered | 

## Example

```python
from pfruck_contabo.models.instance_start_action_response_data import InstanceStartActionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStartActionResponseData from a JSON string
instance_start_action_response_data_instance = InstanceStartActionResponseData.from_json(json)
# print the JSON string representation of the object
print(InstanceStartActionResponseData.to_json())

# convert the object into a dict
instance_start_action_response_data_dict = instance_start_action_response_data_instance.to_dict()
# create an instance of InstanceStartActionResponseData from a dict
instance_start_action_response_data_from_dict = InstanceStartActionResponseData.from_dict(instance_start_action_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


