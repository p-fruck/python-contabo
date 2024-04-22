# ExtraStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssd** | **List[str]** | Specify the size in TB and the quantity | [optional] 
**nvme** | **List[str]** | Specify the size in TB and the quantity | [optional] 

## Example

```python
from pfruck_contabo.models.extra_storage_request import ExtraStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraStorageRequest from a JSON string
extra_storage_request_instance = ExtraStorageRequest.from_json(json)
# print the JSON string representation of the object
print(ExtraStorageRequest.to_json())

# convert the object into a dict
extra_storage_request_dict = extra_storage_request_instance.to_dict()
# create an instance of ExtraStorageRequest from a dict
extra_storage_request_from_dict = ExtraStorageRequest.from_dict(extra_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


