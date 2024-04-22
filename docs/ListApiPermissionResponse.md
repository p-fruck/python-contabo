# ListApiPermissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiPermissionsResponse]**](ApiPermissionsResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_api_permission_response import ListApiPermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListApiPermissionResponse from a JSON string
list_api_permission_response_instance = ListApiPermissionResponse.from_json(json)
# print the JSON string representation of the object
print(ListApiPermissionResponse.to_json())

# convert the object into a dict
list_api_permission_response_dict = list_api_permission_response_instance.to_dict()
# create an instance of ListApiPermissionResponse from a dict
list_api_permission_response_from_dict = ListApiPermissionResponse.from_dict(list_api_permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


