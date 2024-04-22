# PatchInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PatchInstanceResponseData]**](PatchInstanceResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.patch_instance_response import PatchInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInstanceResponse from a JSON string
patch_instance_response_instance = PatchInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(PatchInstanceResponse.to_json())

# convert the object into a dict
patch_instance_response_dict = patch_instance_response_instance.to_dict()
# create an instance of PatchInstanceResponse from a dict
patch_instance_response_from_dict = PatchInstanceResponse.from_dict(patch_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


