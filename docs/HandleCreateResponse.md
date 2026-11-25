# HandleCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HandleResponse]**](HandleResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.handle_create_response import HandleCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandleCreateResponse from a JSON string
handle_create_response_instance = HandleCreateResponse.from_json(json)
# print the JSON string representation of the object
print(HandleCreateResponse.to_json())

# convert the object into a dict
handle_create_response_dict = handle_create_response_instance.to_dict()
# create an instance of HandleCreateResponse from a dict
handle_create_response_from_dict = HandleCreateResponse.from_dict(handle_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


