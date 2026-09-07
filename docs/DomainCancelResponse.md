# DomainCancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainCancel]**](DomainCancel.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_cancel_response import DomainCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCancelResponse from a JSON string
domain_cancel_response_instance = DomainCancelResponse.from_json(json)
# print the JSON string representation of the object
print(DomainCancelResponse.to_json())

# convert the object into a dict
domain_cancel_response_dict = domain_cancel_response_instance.to_dict()
# create an instance of DomainCancelResponse from a dict
domain_cancel_response_from_dict = DomainCancelResponse.from_dict(domain_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


