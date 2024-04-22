# TagAuditResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**id** | **float** | The identifier of the audit entry. | 
**tag_id** | **int** | The identifier of the audit entry. | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**changed_by** | **str** | User ID | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**changes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | List of actual changes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


