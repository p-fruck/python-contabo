# CheckCollectionCheckTemplates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **float** | Id of the check | 
**check_template_id** | **float** | Id of the check template | 
**run_concurrent** | **bool** | Can this check template be run in parallel with other checks | 
**ignore_errors** | **bool** | Will errors be ignored when running this check template | 
**check_templates** | [**List[CheckCollectionCheckTemplates]**](CheckCollectionCheckTemplates.md) | Nested check templates | [optional] 

## Example

```python
from pfruck_contabo.models.check_collection_check_templates import CheckCollectionCheckTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionCheckTemplates from a JSON string
check_collection_check_templates_instance = CheckCollectionCheckTemplates.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionCheckTemplates.to_json())

# convert the object into a dict
check_collection_check_templates_dict = check_collection_check_templates_instance.to_dict()
# create an instance of CheckCollectionCheckTemplates from a dict
check_collection_check_templates_from_dict = CheckCollectionCheckTemplates.from_dict(check_collection_check_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


