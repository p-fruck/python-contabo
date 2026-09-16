# DomainPendingActionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainPendingActionResponse]**](DomainPendingActionResponse.md) | Domains with an unacknowledged outbound transfer | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_pending_actions_list_response import DomainPendingActionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPendingActionsListResponse from a JSON string
domain_pending_actions_list_response_instance = DomainPendingActionsListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainPendingActionsListResponse.to_json())

# convert the object into a dict
domain_pending_actions_list_response_dict = domain_pending_actions_list_response_instance.to_dict()
# create an instance of DomainPendingActionsListResponse from a dict
domain_pending_actions_list_response_from_dict = DomainPendingActionsListResponse.from_dict(domain_pending_actions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


