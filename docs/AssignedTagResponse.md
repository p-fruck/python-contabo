# AssignedTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **float** | Tag&#39;s id | 
**tag_name** | **str** | Tag&#39;s name | 

## Example

```python
from pfruck_contabo.models.assigned_tag_response import AssignedTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedTagResponse from a JSON string
assigned_tag_response_instance = AssignedTagResponse.from_json(json)
# print the JSON string representation of the object
print(AssignedTagResponse.to_json())

# convert the object into a dict
assigned_tag_response_dict = assigned_tag_response_instance.to_dict()
# create an instance of AssignedTagResponse from a dict
assigned_tag_response_from_dict = AssignedTagResponse.from_dict(assigned_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


