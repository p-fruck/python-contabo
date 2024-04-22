# AutoScalingTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the autoscaling for the current object storage. | 
**size_limit_tb** | **float** | Autoscaling size limit for the current object storage. | 

## Example

```python
from pfruck_contabo.models.auto_scaling_type_request import AutoScalingTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoScalingTypeRequest from a JSON string
auto_scaling_type_request_instance = AutoScalingTypeRequest.from_json(json)
# print the JSON string representation of the object
print(AutoScalingTypeRequest.to_json())

# convert the object into a dict
auto_scaling_type_request_dict = auto_scaling_type_request_instance.to_dict()
# create an instance of AutoScalingTypeRequest from a dict
auto_scaling_type_request_from_dict = AutoScalingTypeRequest.from_dict(auto_scaling_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


