# CreateAssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**TagAssignmentSelfLinks**](TagAssignmentSelfLinks.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.create_assignment_response import CreateAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssignmentResponse from a JSON string
create_assignment_response_instance = CreateAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAssignmentResponse.to_json())

# convert the object into a dict
create_assignment_response_dict = create_assignment_response_instance.to_dict()
# create an instance of CreateAssignmentResponse from a dict
create_assignment_response_from_dict = CreateAssignmentResponse.from_dict(create_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


