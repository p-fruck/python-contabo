# PtrRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**ip** | **str** | IP Address | 
**ttl** | **int** | Time to live for the PTR record in seconds | 
**ptr** | **str** | PTR | 

## Example

```python
from pfruck_contabo.models.ptr_record_response import PtrRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PtrRecordResponse from a JSON string
ptr_record_response_instance = PtrRecordResponse.from_json(json)
# print the JSON string representation of the object
print(PtrRecordResponse.to_json())

# convert the object into a dict
ptr_record_response_dict = ptr_record_response_instance.to_dict()
# create an instance of PtrRecordResponse from a dict
ptr_record_response_from_dict = PtrRecordResponse.from_dict(ptr_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


