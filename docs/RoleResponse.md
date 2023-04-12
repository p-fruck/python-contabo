# RoleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Role&#39;s id | 
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**name** | **str** | Role&#39;s name | 
**admin** | **bool** | Admin | 
**access_all_resources** | **bool** | Access All Resources | 
**type** | **str** | Role type can be either &#x60;default&#x60; or &#x60;custom&#x60;. The &#x60;default&#x60; roles cannot be modified or deleted. | 
**permissions** | [**[PermissionResponse]**](PermissionResponse.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


