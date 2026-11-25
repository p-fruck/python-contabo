# CancelDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for cancelling an domain | [optional] 
**reason_text** | **str** | Reason Text when &#x60;Other&#x60; reason got selected while cancelling an domain | [optional] 
**cancel_date** | **datetime** | Date of cancellation | [optional] 

## Example

```python
from pfruck_contabo.models.cancel_domain_request import CancelDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelDomainRequest from a JSON string
cancel_domain_request_instance = CancelDomainRequest.from_json(json)
# print the JSON string representation of the object
print(CancelDomainRequest.to_json())

# convert the object into a dict
cancel_domain_request_dict = cancel_domain_request_instance.to_dict()
# create an instance of CancelDomainRequest from a dict
cancel_domain_request_from_dict = CancelDomainRequest.from_dict(cancel_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


