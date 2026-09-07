# ApiPtrRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PtrRecordResponse]**](PtrRecordResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.api_ptr_record_response import ApiPtrRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPtrRecordResponse from a JSON string
api_ptr_record_response_instance = ApiPtrRecordResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPtrRecordResponse.to_json())

# convert the object into a dict
api_ptr_record_response_dict = api_ptr_record_response_instance.to_dict()
# create an instance of ApiPtrRecordResponse from a dict
api_ptr_record_response_from_dict = ApiPtrRecordResponse.from_dict(api_ptr_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


