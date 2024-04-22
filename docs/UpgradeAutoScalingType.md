# UpgradeAutoScalingType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the autoscaling for the current object storage. | [optional] 
**size_limit_tb** | **float** | Autoscaling size limit for the current object storage. | [optional] 

## Example

```python
from pfruck_contabo.models.upgrade_auto_scaling_type import UpgradeAutoScalingType

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeAutoScalingType from a JSON string
upgrade_auto_scaling_type_instance = UpgradeAutoScalingType.from_json(json)
# print the JSON string representation of the object
print(UpgradeAutoScalingType.to_json())

# convert the object into a dict
upgrade_auto_scaling_type_dict = upgrade_auto_scaling_type_instance.to_dict()
# create an instance of UpgradeAutoScalingType from a dict
upgrade_auto_scaling_type_from_dict = UpgradeAutoScalingType.from_dict(upgrade_auto_scaling_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


