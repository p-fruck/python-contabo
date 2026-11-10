# AccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID of the sub account. | 
**tenant_id** | **str** | Tenant ID of the sub account. | 
**type** | **str** | Customer account type (from customer record). Example values are &#x60;private&#x60; or &#x60;business&#x60;. | 
**company** | **str** | Customer company name (from customer record). | 
**email** | **str** | The email displayed for this account. | 
**first_name** | **str** | First name associated with this account. | 
**last_name** | **str** | Last name associated with this account. | 

## Example

```python
from pfruck_contabo.models.account_details import AccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDetails from a JSON string
account_details_instance = AccountDetails.from_json(json)
# print the JSON string representation of the object
print(AccountDetails.to_json())

# convert the object into a dict
account_details_dict = account_details_instance.to_dict()
# create an instance of AccountDetails from a dict
account_details_from_dict = AccountDetails.from_dict(account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


