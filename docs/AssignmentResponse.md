# AssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**tag_id** | **int** | The identifier of the tag. | 
**tag_name** | **str** | Tag&#39;s name | 
**resource_type** | **str** | Resource type. Resource type is one of &#x60;instance|image|object-storage&#x60;. | 
**resource_id** | **str** | Resource id | 
**resource_name** | **str** | Resource name | 

## Example

```python
from pfruck_contabo.models.assignment_response import AssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentResponse from a JSON string
assignment_response_instance = AssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(AssignmentResponse.to_json())

# convert the object into a dict
assignment_response_dict = assignment_response_instance.to_dict()
# create an instance of AssignmentResponse from a dict
assignment_response_from_dict = AssignmentResponse.from_dict(assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


