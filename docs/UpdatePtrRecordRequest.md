# UpdatePtrRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptr** | **str** | PTR Record name | 

## Example

```python
from pfruck_contabo.models.update_ptr_record_request import UpdatePtrRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePtrRecordRequest from a JSON string
update_ptr_record_request_instance = UpdatePtrRecordRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePtrRecordRequest.to_json())

# convert the object into a dict
update_ptr_record_request_dict = update_ptr_record_request_instance.to_dict()
# create an instance of UpdatePtrRecordRequest from a dict
update_ptr_record_request_from_dict = UpdatePtrRecordRequest.from_dict(update_ptr_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


