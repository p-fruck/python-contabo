# ExtChecksGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExtCheckResponse]**](ExtCheckResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.ext_checks_get_response import ExtChecksGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtChecksGetResponse from a JSON string
ext_checks_get_response_instance = ExtChecksGetResponse.from_json(json)
# print the JSON string representation of the object
print(ExtChecksGetResponse.to_json())

# convert the object into a dict
ext_checks_get_response_dict = ext_checks_get_response_instance.to_dict()
# create an instance of ExtChecksGetResponse from a dict
ext_checks_get_response_from_dict = ExtChecksGetResponse.from_dict(ext_checks_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


