# CheckCollectionTemplatesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CheckCollectionTemplateResponse]**](CheckCollectionTemplateResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.check_collection_templates_get_response import CheckCollectionTemplatesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionTemplatesGetResponse from a JSON string
check_collection_templates_get_response_instance = CheckCollectionTemplatesGetResponse.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionTemplatesGetResponse.to_json())

# convert the object into a dict
check_collection_templates_get_response_dict = check_collection_templates_get_response_instance.to_dict()
# create an instance of CheckCollectionTemplatesGetResponse from a dict
check_collection_templates_get_response_from_dict = CheckCollectionTemplatesGetResponse.from_dict(check_collection_templates_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


