# TagAssignmentSelfLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Link to current resource. | 
**tag** | **str** | Link to related tag. | 
**resource** | **str** | Link to assigned resource | 

## Example

```python
from pfruck_contabo.models.tag_assignment_self_links import TagAssignmentSelfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TagAssignmentSelfLinks from a JSON string
tag_assignment_self_links_instance = TagAssignmentSelfLinks.from_json(json)
# print the JSON string representation of the object
print(TagAssignmentSelfLinks.to_json())

# convert the object into a dict
tag_assignment_self_links_dict = tag_assignment_self_links_instance.to_dict()
# create an instance of TagAssignmentSelfLinks from a dict
tag_assignment_self_links_from_dict = TagAssignmentSelfLinks.from_dict(tag_assignment_self_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


