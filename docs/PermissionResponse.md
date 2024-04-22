# PermissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | API endpoint. In order to get a list availbale api enpoints please refer to the GET api-permissions endpoint. | 
**actions** | **List[str]** | Action allowed for the API endpoint. Basically &#x60;CREATE&#x60; corresponds to POST endpoints, &#x60;READ&#x60; to GET endpoints, &#x60;UPDATE&#x60; to PATCH / PUT endpoints and &#x60;DELETE&#x60; to DELETE endpoints. | 
**resources** | [**List[ResourcePermissionsResponse]**](ResourcePermissionsResponse.md) |  | [optional] 

## Example

```python
from pfruck_contabo.models.permission_response import PermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionResponse from a JSON string
permission_response_instance = PermissionResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionResponse.to_json())

# convert the object into a dict
permission_response_dict = permission_response_instance.to_dict()
# create an instance of PermissionResponse from a dict
permission_response_from_dict = PermissionResponse.from_dict(permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


