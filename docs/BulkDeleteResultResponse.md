# BulkDeleteResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**failed_ids** | **List[int]** | Failed zone record IDs | 

## Example

```python
from pfruck_contabo.models.bulk_delete_result_response import BulkDeleteResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteResultResponse from a JSON string
bulk_delete_result_response_instance = BulkDeleteResultResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteResultResponse.to_json())

# convert the object into a dict
bulk_delete_result_response_dict = bulk_delete_result_response_instance.to_dict()
# create an instance of BulkDeleteResultResponse from a dict
bulk_delete_result_response_from_dict = BulkDeleteResultResponse.from_dict(bulk_delete_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


