# DomainResponseStatusError

Customer-facing reason a domain ended up in a failed state, or null when there is no error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from pfruck_contabo.models.domain_response_status_error import DomainResponseStatusError

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponseStatusError from a JSON string
domain_response_status_error_instance = DomainResponseStatusError.from_json(json)
# print the JSON string representation of the object
print(DomainResponseStatusError.to_json())

# convert the object into a dict
domain_response_status_error_dict = domain_response_status_error_instance.to_dict()
# create an instance of DomainResponseStatusError from a dict
domain_response_status_error_from_dict = DomainResponseStatusError.from_dict(domain_response_status_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


