# HandleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**handle_id** | **str** | Handle ID | 
**handle_type** | **str** | Handle Type | 
**is_default** | **bool** | Flag if the handle is default or not | 
**alias** | **str** | Customer-chosen alias for the handle. Unique per customer. | [optional] 
**first_name** | **str** | Handle first name | 
**last_name** | **str** | Handle last name | 
**organization** | **str** | The organization of the handle | [optional] 
**email** | **str** | Handle email | 
**gender** | **str** | Handle gender | 
**birth_info** | [**HandleBirthInfo**](HandleBirthInfo.md) | The birth info of the handle | [optional] 
**address** | [**HandleAddress**](HandleAddress.md) | Address details for handle | 
**phone** | [**HandlePhone**](HandlePhone.md) | Handle phone | 
**fax** | [**HandlePhone**](HandlePhone.md) | Handle fax | [optional] 
**nic_it_entity_type** | **str** | NIC.it entity type. Present for .it registrant contacts. Valid values: natural_person, individual_firm, non_profit, public_org, other, company, foreign_legal_entity. | [optional] 
**pin** | **str** | Registration code / fiscal code. Present for .it registrant contacts (NIC.it NIC_IT_REG_CODE — codice fiscale or VAT number). | [optional] 
**legal_status** | **str** | Legal status of an organization handle. Present for organization handles; sent to AFNIC as AFNIC_PM_LEGAL_STATUS for .fr contacts. | [optional] 
**sidn_legal_form** | **str** | SIDN legal form. Present for .nl contacts that have one set. Free-form per the SIDN schema — e.g. BV, NV, Stichting, Eenmanszaak, VOF. | [optional] 
**sidn_legal_form_reg_no** | **str** | SIDN legal form registration number (KvK number). Present for .nl contacts that have one set. | [optional] 

## Example

```python
from pfruck_contabo.models.handle_response import HandleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandleResponse from a JSON string
handle_response_instance = HandleResponse.from_json(json)
# print the JSON string representation of the object
print(HandleResponse.to_json())

# convert the object into a dict
handle_response_dict = handle_response_instance.to_dict()
# create an instance of HandleResponse from a dict
handle_response_from_dict = HandleResponse.from_dict(handle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


