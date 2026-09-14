# ExtCheckCollectionTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_collection_template_id** | **float** | Check collection template&#39;s id | 
**name** | **str** | Name of the check collection template | 
**description** | **str** | Description for the check collection template | 
**internal** | **bool** | Is check collection only internal (not shown to the customer) | 
**object_type** | **str** | Object type for which the check collection template can be used | 
**check_templates** | [**List[CheckCollectionTemplatesCheckTemplates]**](CheckCollectionTemplatesCheckTemplates.md) | Check templates which are part of this collection template | 
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**tenant_id** | **str** | Tenant id | 
**customer_id** | **str** | Customer id | 

## Example

```python
from pfruck_contabo.models.ext_check_collection_template_response import ExtCheckCollectionTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtCheckCollectionTemplateResponse from a JSON string
ext_check_collection_template_response_instance = ExtCheckCollectionTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ExtCheckCollectionTemplateResponse.to_json())

# convert the object into a dict
ext_check_collection_template_response_dict = ext_check_collection_template_response_instance.to_dict()
# create an instance of ExtCheckCollectionTemplateResponse from a dict
ext_check_collection_template_response_from_dict = ExtCheckCollectionTemplateResponse.from_dict(ext_check_collection_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


