# HandlePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Customer-chosen alias for the handle. Unique per customer (exact, case-sensitive). Optional for now. | [optional] 
**email** | **str** | Handle email | 
**gender** | **str** | Handle gender | 
**birth_info** | [**HandleBirthInfo**](HandleBirthInfo.md) | The birth info of the handle | [optional] 
**address** | [**HandleAddress**](HandleAddress.md) | Address details for handle | 
**phone** | [**HandlePhone**](HandlePhone.md) | Handle phone | 
**fax** | [**HandlePhone**](HandlePhone.md) | Handle fax | [optional] 
**nic_it_entity_type** | **str** | NIC.it entity type (required for .it registrant contacts). Valid values: natural_person, individual_firm, non_profit, public_org, other, company, foreign_legal_entity. | [optional] 
**legal_status** | **str** | Legal status of an organization handle. Applies to organization handles only and is ignored for person handles. Sent to AFNIC as AFNIC_PM_LEGAL_STATUS, which is required for every .fr contact. Defaults to company when omitted. | [optional] 
**pin** | **str** | Registration code / fiscal code. Required for .it registrant contacts (NIC.it NIC_IT_REG_CODE — codice fiscale or VAT number). | [optional] 
**sidn_legal_form** | **str** | SIDN legal form for .nl contacts (SIDN_LEGAL_FORM). Free-form per the SIDN schema — e.g. BV, NV, Stichting, Eenmanszaak, VOF. | [optional] 
**sidn_legal_form_reg_no** | **str** | SIDN legal form registration number for .nl contacts (KvK / Chamber of Commerce number, SIDN_LEGAL_REG_NO). | [optional] 

## Example

```python
from pfruck_contabo.models.handle_patch_request import HandlePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HandlePatchRequest from a JSON string
handle_patch_request_instance = HandlePatchRequest.from_json(json)
# print the JSON string representation of the object
print(HandlePatchRequest.to_json())

# convert the object into a dict
handle_patch_request_dict = handle_patch_request_instance.to_dict()
# create an instance of HandlePatchRequest from a dict
handle_patch_request_from_dict = HandlePatchRequest.from_dict(handle_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


