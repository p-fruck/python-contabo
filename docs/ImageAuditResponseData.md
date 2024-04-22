# ImageAuditResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the audit entry. | 
**action** | **str** | Type of the action. | 
**timestamp** | **datetime** | When the change took place. | 
**tenant_id** | **str** | Customer tenant id | 
**customer_id** | **str** | Customer ID | 
**changed_by** | **str** | Id of user who performed the change | 
**username** | **str** | Name of the user which led to the change. | 
**request_id** | **str** | The requestId of the API call which led to the change. | 
**trace_id** | **str** | The traceId of the API call which led to the change. | 
**image_id** | **str** | The identifier of the image | 
**changes** | **object** | List of actual changes. | [optional] 

## Example

```python
from pfruck_contabo.models.image_audit_response_data import ImageAuditResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAuditResponseData from a JSON string
image_audit_response_data_instance = ImageAuditResponseData.from_json(json)
# print the JSON string representation of the object
print(ImageAuditResponseData.to_json())

# convert the object into a dict
image_audit_response_data_dict = image_audit_response_data_instance.to_dict()
# create an instance of ImageAuditResponseData from a dict
image_audit_response_data_from_dict = ImageAuditResponseData.from_dict(image_audit_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


