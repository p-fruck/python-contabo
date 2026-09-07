# RemedyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal** | **bool** | Is internal (not shown to the customer) | 
**status** | **str** | Status of the handle | 
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**remedy_id** | **float** | Remedy&#39;s id | 
**remedy_collection_id** | **float** | ID of remedy collection if started in scope of a collection | 
**remedy_template_id** | **float** | Remedy Template for this remedy | 
**name** | **str** | Name of this remedy template | 
**note** | **str** | Translation key for the customer-facing remedy note. Possible values: fail_remedy_failed, success_remedy_successful, remedy_internal_error, instance_firewall_detach_successful, instance_live_migration_successful, instance_reboot_successful | 
**internal_note** | **str** | Translation key for the internal-only remedy note (agent view). Possible values: remedy_internal_error_internal, instance_firewall_detach_successful_internal, instance_live_migration_successful_internal, instance_reboot_successful_internal | 
**duration_ms** | **float** | Duration of the remedy in milliseconds | 
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 
**log** | **str** | Detailed log of the check execution | 

## Example

```python
from pfruck_contabo.models.remedy_response import RemedyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemedyResponse from a JSON string
remedy_response_instance = RemedyResponse.from_json(json)
# print the JSON string representation of the object
print(RemedyResponse.to_json())

# convert the object into a dict
remedy_response_dict = remedy_response_instance.to_dict()
# create an instance of RemedyResponse from a dict
remedy_response_from_dict = RemedyResponse.from_dict(remedy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


