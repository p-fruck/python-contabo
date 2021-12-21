# RoleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Role&#x27;s id | 
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**name** | **str** | Role Name | 
**role_type** | **str** | Role type can be either &#x60;resourcePermission&#x60; for accessing specific resources or &#x60;apiPermission&#x60; for accessing specific API endpoints. | 
**api_permissions** | [**list[ApiPermissionsResponse]**](ApiPermissionsResponse.md) | API Permissions array | 
**resource_permissions** | [**list[ResourcePermissionsResponse]**](ResourcePermissionsResponse.md) | Resource Permissions array | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

