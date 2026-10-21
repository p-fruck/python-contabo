# DomainPendingActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**domain_id** | **str** | OpusDNS domain id (mirrors the local domain &#x60;opusId&#x60;) | 
**domain** | **str** | Domain name (sld.tld) | 
**event_type** | **str** | Event type — always OUTBOUND_TRANSFER for this endpoint | 
**event_id** | **str** | OpusDNS event id to ACK/NACK against | 
**created_on** | **datetime** | When OpusDNS created the transfer-out event | 

## Example

```python
from pfruck_contabo.models.domain_pending_action_response import DomainPendingActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPendingActionResponse from a JSON string
domain_pending_action_response_instance = DomainPendingActionResponse.from_json(json)
# print the JSON string representation of the object
print(DomainPendingActionResponse.to_json())

# convert the object into a dict
domain_pending_action_response_dict = domain_pending_action_response_instance.to_dict()
# create an instance of DomainPendingActionResponse from a dict
domain_pending_action_response_from_dict = DomainPendingActionResponse.from_dict(domain_pending_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


