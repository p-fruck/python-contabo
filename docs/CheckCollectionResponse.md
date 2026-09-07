# CheckCollectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal** | **bool** | Is internal (not shown to the customer) | 
**status** | **str** | Status of the handle | 
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**check_collection_id** | **float** | Check collection&#39;s id | 
**check_collection_template_id** | **float** | Check Collection Template for this check collection | 
**check_templates** | [**List[CheckCollectionCheckTemplates]**](CheckCollectionCheckTemplates.md) | Check templates which are part of this collection template | 
**created_date** | **datetime** | Creation date | 
**modified_date** | **datetime** | Modify date | 
**org_id** | **str** | Org id | 
**account_id** | **str** | Account id | 
**checks** | [**List[CheckResponse]**](CheckResponse.md) | Checks performed in this check collection | 

## Example

```python
from pfruck_contabo.models.check_collection_response import CheckCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionResponse from a JSON string
check_collection_response_instance = CheckCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionResponse.to_json())

# convert the object into a dict
check_collection_response_dict = check_collection_response_instance.to_dict()
# create an instance of CheckCollectionResponse from a dict
check_collection_response_from_dict = CheckCollectionResponse.from_dict(check_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


