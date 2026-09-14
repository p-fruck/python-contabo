# CheckTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 
**check_template_id** | **float** | Check template&#39;s id | 
**name** | **str** | Name of the check template | 
**description** | **str** | Description for the check template | 
**internal** | **bool** | Is check only internal (not shown to the customer) | 
**object_type** | **str** | Object type for which the check template can be used | 
**collector_class** | **str** | Class used to collect the required information for the check | 
**check_class** | **str** | Class used to perform the check | 
**remedy_template_ids** | **List[str]** | Remedy Template IDs that are related to this remedy | 

## Example

```python
from pfruck_contabo.models.check_template_response import CheckTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTemplateResponse from a JSON string
check_template_response_instance = CheckTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(CheckTemplateResponse.to_json())

# convert the object into a dict
check_template_response_dict = check_template_response_instance.to_dict()
# create an instance of CheckTemplateResponse from a dict
check_template_response_from_dict = CheckTemplateResponse.from_dict(check_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


