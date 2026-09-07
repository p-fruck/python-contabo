# RemedyTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 
**remedy_template_id** | **float** | Remedy template&#39;s id | 
**name** | **str** | Name of the remedy template | 
**description** | **str** | Description for the remedy template | 
**internal** | **bool** | Is remedy only internal (not shown to the customer) | 
**object_type** | **str** | Object type for which the remedy template can be used | 
**collector_class** | **str** | Class used to collect the required information for the remedy | 
**remedy_class** | **str** | Class used to perform the remedy | 
**requirements** | **object** | Requirements for remedy (reboot, reinstall, ...) | 
**check_template_ids** | **List[str]** | Check Template IDs that are related to this remedy | 

## Example

```python
from pfruck_contabo.models.remedy_template_response import RemedyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemedyTemplateResponse from a JSON string
remedy_template_response_instance = RemedyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(RemedyTemplateResponse.to_json())

# convert the object into a dict
remedy_template_response_dict = remedy_template_response_instance.to_dict()
# create an instance of RemedyTemplateResponse from a dict
remedy_template_response_from_dict = RemedyTemplateResponse.from_dict(remedy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


