# CreateTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The ticket subject | 
**note** | **str** | The ticket note | 
**sender** | **str** | Customer email | 

## Example

```python
from pfruck_contabo.models.create_ticket_request import CreateTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketRequest from a JSON string
create_ticket_request_instance = CreateTicketRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTicketRequest.to_json())

# convert the object into a dict
create_ticket_request_dict = create_ticket_request_instance.to_dict()
# create an instance of CreateTicketRequest from a dict
create_ticket_request_from_dict = CreateTicketRequest.from_dict(create_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


