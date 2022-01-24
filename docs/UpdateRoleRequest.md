# UpdateRoleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the role. There is a limit of 255 characters per role. | 
**admin** | **bool** | If user is admin he will have permissions to all API endpoints and resources. Enabling this will superseed all role definitions and &#x60;accessAllResources&#x60;. | 
**access_all_resources** | **bool** | Allow access to all resources. This will superseed all assigned resources in a role | 
**permissions** | [**list[PermissionRequest]**](PermissionRequest.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

