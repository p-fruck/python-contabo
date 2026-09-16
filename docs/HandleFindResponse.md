# HandleFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HandleResponse]**](HandleResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.handle_find_response import HandleFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandleFindResponse from a JSON string
handle_find_response_instance = HandleFindResponse.from_json(json)
# print the JSON string representation of the object
print(HandleFindResponse.to_json())

# convert the object into a dict
handle_find_response_dict = handle_find_response_instance.to_dict()
# create an instance of HandleFindResponse from a dict
handle_find_response_from_dict = HandleFindResponse.from_dict(handle_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


