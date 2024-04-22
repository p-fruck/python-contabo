# ResourcePermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **int** | Tag&#39;s id | 
**tag_name** | **str** | Tag name. The resriction is based on the resources which have been assigned to that tag. If no resource has been assigned to the given tag, no access will be possible. | 

## Example

```python
from pfruck_contabo.models.resource_permissions_response import ResourcePermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePermissionsResponse from a JSON string
resource_permissions_response_instance = ResourcePermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(ResourcePermissionsResponse.to_json())

# convert the object into a dict
resource_permissions_response_dict = resource_permissions_response_instance.to_dict()
# create an instance of ResourcePermissionsResponse from a dict
resource_permissions_response_from_dict = ResourcePermissionsResponse.from_dict(resource_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


