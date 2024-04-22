# AutoScalingTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the autoscaling for the current object storage. | 
**size_limit_tb** | **float** | Autoscaling size limit for the current object storage. | 
**error_message** | **str** | Error message | [optional] 

## Example

```python
from pfruck_contabo.models.auto_scaling_type_response import AutoScalingTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoScalingTypeResponse from a JSON string
auto_scaling_type_response_instance = AutoScalingTypeResponse.from_json(json)
# print the JSON string representation of the object
print(AutoScalingTypeResponse.to_json())

# convert the object into a dict
auto_scaling_type_response_dict = auto_scaling_type_response_instance.to_dict()
# create an instance of AutoScalingTypeResponse from a dict
auto_scaling_type_response_from_dict = AutoScalingTypeResponse.from_dict(auto_scaling_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


