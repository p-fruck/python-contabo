# ExtCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal** | **bool** | Is internal (not shown to the customer) | 
**status** | **str** | Status of the handle | 
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**check_id** | **float** | Check&#39;s id | 
**check_collection_id** | **float** | ID of check collection if started in scope of a collection | 
**check_template_id** | **float** | Check Template for this check | 
**name** | **str** | Name of this check template | 
**note** | **str** | Note to be shown to the customer | 
**internal_note** | **str** | Note which is shown only internally to the agent | 
**duration_ms** | **float** | Duration of the check in milliseconds | 
**remedy_templates** | [**List[RemedyTemplateSummary]**](RemedyTemplateSummary.md) | Remedy templates linked to this check template | 
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**tenant_id** | **str** | Tenant id | 
**customer_id** | **str** | Customer id | 

## Example

```python
from pfruck_contabo.models.ext_check_response import ExtCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtCheckResponse from a JSON string
ext_check_response_instance = ExtCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ExtCheckResponse.to_json())

# convert the object into a dict
ext_check_response_dict = ext_check_response_instance.to_dict()
# create an instance of ExtCheckResponse from a dict
ext_check_response_from_dict = ExtCheckResponse.from_dict(ext_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


