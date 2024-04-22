# PatchVncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnc_password** | **str** | Password for instance VNC | 

## Example

```python
from pfruck_contabo.models.patch_vnc_request import PatchVncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchVncRequest from a JSON string
patch_vnc_request_instance = PatchVncRequest.from_json(json)
# print the JSON string representation of the object
print(PatchVncRequest.to_json())

# convert the object into a dict
patch_vnc_request_dict = patch_vnc_request_instance.to_dict()
# create an instance of PatchVncRequest from a dict
patch_vnc_request_from_dict = PatchVncRequest.from_dict(patch_vnc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


