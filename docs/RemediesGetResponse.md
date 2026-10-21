# RemediesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RemedyResponse]**](RemedyResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.remedies_get_response import RemediesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemediesGetResponse from a JSON string
remedies_get_response_instance = RemediesGetResponse.from_json(json)
# print the JSON string representation of the object
print(RemediesGetResponse.to_json())

# convert the object into a dict
remedies_get_response_dict = remedies_get_response_instance.to_dict()
# create an instance of RemediesGetResponse from a dict
remedies_get_response_from_dict = RemediesGetResponse.from_dict(remedies_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


