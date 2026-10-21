# InstanceAssignmentSelfLinks1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to current resource. | 
**firewall** | **str** | Link to related firewall. | 
**instance** | **str** | Link to assigned instance. | 

## Example

```python
from pfruck_contabo.models.instance_assignment_self_links1 import InstanceAssignmentSelfLinks1

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceAssignmentSelfLinks1 from a JSON string
instance_assignment_self_links1_instance = InstanceAssignmentSelfLinks1.from_json(json)
# print the JSON string representation of the object
print(InstanceAssignmentSelfLinks1.to_json())

# convert the object into a dict
instance_assignment_self_links1_dict = instance_assignment_self_links1_instance.to_dict()
# create an instance of InstanceAssignmentSelfLinks1 from a dict
instance_assignment_self_links1_from_dict = InstanceAssignmentSelfLinks1.from_dict(instance_assignment_self_links1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


