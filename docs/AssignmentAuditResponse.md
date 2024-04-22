# AssignmentAuditResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**id** | **float** | The identifier of the audit entry. | 
**resource_id** | **str** | Resource&#39;s id | 
**resource_type** | **str** | Resource type. Resource type is one of &#x60;instance|image|object-storage&#x60;. | 
**tag_id** | **int** | Tag&#39;s id | 
**action** | **str** | Audit Action | 
**timestamp** | **datetime** | Audit creation date | 
**changed_by** | **str** | User ID | 
**username** | **str** | User Full Name | 
**request_id** | **str** | Request ID | 
**trace_id** | **str** | Trace ID | 
**changes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Changes made for a specific Tag | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


