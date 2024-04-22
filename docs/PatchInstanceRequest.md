# PatchInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the instance | [optional] 

## Example

```python
from pfruck_contabo.models.patch_instance_request import PatchInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInstanceRequest from a JSON string
patch_instance_request_instance = PatchInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchInstanceRequest.to_json())

# convert the object into a dict
patch_instance_request_dict = patch_instance_request_instance.to_dict()
# create an instance of PatchInstanceRequest from a dict
patch_instance_request_from_dict = PatchInstanceRequest.from_dict(patch_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


