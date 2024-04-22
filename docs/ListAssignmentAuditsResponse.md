# ListAssignmentAuditsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[AssignmentAuditResponse]**](AssignmentAuditResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_assignment_audits_response import ListAssignmentAuditsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAssignmentAuditsResponse from a JSON string
list_assignment_audits_response_instance = ListAssignmentAuditsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAssignmentAuditsResponse.to_json())

# convert the object into a dict
list_assignment_audits_response_dict = list_assignment_audits_response_instance.to_dict()
# create an instance of ListAssignmentAuditsResponse from a dict
list_assignment_audits_response_from_dict = ListAssignmentAuditsResponse.from_dict(list_assignment_audits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


