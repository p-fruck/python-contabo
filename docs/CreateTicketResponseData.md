# CreateTicketResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 

## Example

```python
from pfruck_contabo.models.create_ticket_response_data import CreateTicketResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketResponseData from a JSON string
create_ticket_response_data_instance = CreateTicketResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateTicketResponseData.to_json())

# convert the object into a dict
create_ticket_response_data_dict = create_ticket_response_data_instance.to_dict()
# create an instance of CreateTicketResponseData from a dict
create_ticket_response_data_from_dict = CreateTicketResponseData.from_dict(create_ticket_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


