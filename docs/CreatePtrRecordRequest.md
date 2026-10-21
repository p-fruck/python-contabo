# CreatePtrRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptr** | **str** | PTR Record name | 
**ip** | **str** | IP Address | 
**ttl** | **int** | Time to live for the PTR record in seconds | 

## Example

```python
from pfruck_contabo.models.create_ptr_record_request import CreatePtrRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePtrRecordRequest from a JSON string
create_ptr_record_request_instance = CreatePtrRecordRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePtrRecordRequest.to_json())

# convert the object into a dict
create_ptr_record_request_dict = create_ptr_record_request_instance.to_dict()
# create an instance of CreatePtrRecordRequest from a dict
create_ptr_record_request_from_dict = CreatePtrRecordRequest.from_dict(create_ptr_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


