# AccountOrgResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 

## Example

```python
from pfruck_contabo.models.account_org_response import AccountOrgResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOrgResponse from a JSON string
account_org_response_instance = AccountOrgResponse.from_json(json)
# print the JSON string representation of the object
print(AccountOrgResponse.to_json())

# convert the object into a dict
account_org_response_dict = account_org_response_instance.to_dict()
# create an instance of AccountOrgResponse from a dict
account_org_response_from_dict = AccountOrgResponse.from_dict(account_org_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


