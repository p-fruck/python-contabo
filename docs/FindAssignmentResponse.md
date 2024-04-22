# FindAssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AssignmentResponse]**](AssignmentResponse.md) |  | 
**links** | [**TagAssignmentSelfLinks**](TagAssignmentSelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_assignment_response import FindAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindAssignmentResponse from a JSON string
find_assignment_response_instance = FindAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(FindAssignmentResponse.to_json())

# convert the object into a dict
find_assignment_response_dict = find_assignment_response_instance.to_dict()
# create an instance of FindAssignmentResponse from a dict
find_assignment_response_from_dict = FindAssignmentResponse.from_dict(find_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


