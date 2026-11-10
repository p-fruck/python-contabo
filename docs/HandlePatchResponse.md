# HandlePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HandleResponse]**](HandleResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.handle_patch_response import HandlePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandlePatchResponse from a JSON string
handle_patch_response_instance = HandlePatchResponse.from_json(json)
# print the JSON string representation of the object
print(HandlePatchResponse.to_json())

# convert the object into a dict
handle_patch_response_dict = handle_patch_response_instance.to_dict()
# create an instance of HandlePatchResponse from a dict
handle_patch_response_from_dict = HandlePatchResponse.from_dict(handle_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


