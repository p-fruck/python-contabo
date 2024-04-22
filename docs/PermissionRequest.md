# PermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | The name of the role. There is a limit of 255 characters per role. | 
**actions** | **List[str]** | Action allowed for the API endpoint. Basically &#x60;CREATE&#x60; corresponds to POST endpoints, &#x60;READ&#x60; to GET endpoints, &#x60;UPDATE&#x60; to PATCH / PUT endpoints and &#x60;DELETE&#x60; to DELETE endpoints. | 
**resources** | **List[int]** | The IDs of tags. Only if those tags are assgined to a resource the user with that role will be able to access the resource. | [optional] 

## Example

```python
from pfruck_contabo.models.permission_request import PermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionRequest from a JSON string
permission_request_instance = PermissionRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionRequest.to_json())

# convert the object into a dict
permission_request_dict = permission_request_instance.to_dict()
# create an instance of PermissionRequest from a dict
permission_request_from_dict = PermissionRequest.from_dict(permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


