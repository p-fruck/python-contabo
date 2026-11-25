# SetDefaultHandleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HandleResponse]**](HandleResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.set_default_handle_response import SetDefaultHandleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultHandleResponse from a JSON string
set_default_handle_response_instance = SetDefaultHandleResponse.from_json(json)
# print the JSON string representation of the object
print(SetDefaultHandleResponse.to_json())

# convert the object into a dict
set_default_handle_response_dict = set_default_handle_response_instance.to_dict()
# create an instance of SetDefaultHandleResponse from a dict
set_default_handle_response_from_dict = SetDefaultHandleResponse.from_dict(set_default_handle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


