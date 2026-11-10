# CheckTemplatesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CheckTemplateResponse]**](CheckTemplateResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.check_templates_get_response import CheckTemplatesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTemplatesGetResponse from a JSON string
check_templates_get_response_instance = CheckTemplatesGetResponse.from_json(json)
# print the JSON string representation of the object
print(CheckTemplatesGetResponse.to_json())

# convert the object into a dict
check_templates_get_response_dict = check_templates_get_response_instance.to_dict()
# create an instance of CheckTemplatesGetResponse from a dict
check_templates_get_response_from_dict = CheckTemplatesGetResponse.from_dict(check_templates_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


