# RoleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Role&#x27;s id | 
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**name** | **str** | Role Name | 
**admin** | **bool** | Admin | 
**access_all_resources** | **bool** | Access All Resources | 
**type** | **str** | Role type can be either &#x60;default&#x60; or &#x60;custom&#x60;. The &#x60;default&#x60; roles cannot be modified or deleted | 
**permissions** | [**list[PermissionResponse]**](PermissionResponse.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

