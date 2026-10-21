# RemedyTemplatesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RemedyTemplateResponse]**](RemedyTemplateResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.remedy_templates_get_response import RemedyTemplatesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemedyTemplatesGetResponse from a JSON string
remedy_templates_get_response_instance = RemedyTemplatesGetResponse.from_json(json)
# print the JSON string representation of the object
print(RemedyTemplatesGetResponse.to_json())

# convert the object into a dict
remedy_templates_get_response_dict = remedy_templates_get_response_instance.to_dict()
# create an instance of RemedyTemplatesGetResponse from a dict
remedy_templates_get_response_from_dict = RemedyTemplatesGetResponse.from_dict(remedy_templates_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


