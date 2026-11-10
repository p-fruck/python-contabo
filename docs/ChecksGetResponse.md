# ChecksGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CheckResponse]**](CheckResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.checks_get_response import ChecksGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksGetResponse from a JSON string
checks_get_response_instance = ChecksGetResponse.from_json(json)
# print the JSON string representation of the object
print(ChecksGetResponse.to_json())

# convert the object into a dict
checks_get_response_dict = checks_get_response_instance.to_dict()
# create an instance of ChecksGetResponse from a dict
checks_get_response_from_dict = ChecksGetResponse.from_dict(checks_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


