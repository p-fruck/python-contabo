# InstanceAssignmentSelfLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to current resource. | 
**virtual_private_cloud** | **str** | Link to related Private Network. | 
**instance** | **str** | Link to assigned instance. | 

## Example

```python
from pfruck_contabo.models.instance_assignment_self_links import InstanceAssignmentSelfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceAssignmentSelfLinks from a JSON string
instance_assignment_self_links_instance = InstanceAssignmentSelfLinks.from_json(json)
# print the JSON string representation of the object
print(InstanceAssignmentSelfLinks.to_json())

# convert the object into a dict
instance_assignment_self_links_dict = instance_assignment_self_links_instance.to_dict()
# create an instance of InstanceAssignmentSelfLinks from a dict
instance_assignment_self_links_from_dict = InstanceAssignmentSelfLinks.from_dict(instance_assignment_self_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


