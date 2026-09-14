# ExtCheckCollectionTemplatesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExtCheckCollectionTemplateResponse]**](ExtCheckCollectionTemplateResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.ext_check_collection_templates_get_response import ExtCheckCollectionTemplatesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtCheckCollectionTemplatesGetResponse from a JSON string
ext_check_collection_templates_get_response_instance = ExtCheckCollectionTemplatesGetResponse.from_json(json)
# print the JSON string representation of the object
print(ExtCheckCollectionTemplatesGetResponse.to_json())

# convert the object into a dict
ext_check_collection_templates_get_response_dict = ext_check_collection_templates_get_response_instance.to_dict()
# create an instance of ExtCheckCollectionTemplatesGetResponse from a dict
ext_check_collection_templates_get_response_from_dict = ExtCheckCollectionTemplatesGetResponse.from_dict(ext_check_collection_templates_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


