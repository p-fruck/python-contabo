# DomainSuggestionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainSuggestion]**](DomainSuggestion.md) | The list of domain suggestions. | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_suggestions_list_response import DomainSuggestionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainSuggestionsListResponse from a JSON string
domain_suggestions_list_response_instance = DomainSuggestionsListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainSuggestionsListResponse.to_json())

# convert the object into a dict
domain_suggestions_list_response_dict = domain_suggestions_list_response_instance.to_dict()
# create an instance of DomainSuggestionsListResponse from a dict
domain_suggestions_list_response_from_dict = DomainSuggestionsListResponse.from_dict(domain_suggestions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


