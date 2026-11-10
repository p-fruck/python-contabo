# ExtRemediesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExtRemedyResponse]**](ExtRemedyResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.ext_remedies_get_response import ExtRemediesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtRemediesGetResponse from a JSON string
ext_remedies_get_response_instance = ExtRemediesGetResponse.from_json(json)
# print the JSON string representation of the object
print(ExtRemediesGetResponse.to_json())

# convert the object into a dict
ext_remedies_get_response_dict = ext_remedies_get_response_instance.to_dict()
# create an instance of ExtRemediesGetResponse from a dict
ext_remedies_get_response_from_dict = ExtRemediesGetResponse.from_dict(ext_remedies_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


