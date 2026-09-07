# RemedyTemplateSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Remedy template id | 
**name** | **str** | Translation key for the remedy name. Possible values: dummy_remedy_name, success_remedy_name, fail_remedy_name, instance_restart_remedy_name, instance_firewall_detach_remedy_name, instance_live_migration_remedy_name | 
**description** | **str** | Translation key for the remedy description. Possible values: dummy_remedy_description, success_remedy_description, fail_remedy_description, instance_restart_remedy_description, instance_firewall_detach_remedy_description, instance_live_migration_remedy_description | 

## Example

```python
from pfruck_contabo.models.remedy_template_summary import RemedyTemplateSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RemedyTemplateSummary from a JSON string
remedy_template_summary_instance = RemedyTemplateSummary.from_json(json)
# print the JSON string representation of the object
print(RemedyTemplateSummary.to_json())

# convert the object into a dict
remedy_template_summary_dict = remedy_template_summary_instance.to_dict()
# create an instance of RemedyTemplateSummary from a dict
remedy_template_summary_from_dict = RemedyTemplateSummary.from_dict(remedy_template_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


