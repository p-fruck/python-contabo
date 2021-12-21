# UpdateRoleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the role. There is a limit of 255 characters per role. | 
**api_permissions** | [**list[ApiPermissionsResponse]**](ApiPermissionsResponse.md) |  | [optional] 
**resource_permissions** | **list[int]** | The IDs of tags. Only if those tags are assgined to a resource the user with that role will be able to access the resource. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

