# CreateObjectStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateObjectStorageResponseData]**](CreateObjectStorageResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_object_storage_response import CreateObjectStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectStorageResponse from a JSON string
create_object_storage_response_instance = CreateObjectStorageResponse.from_json(json)
# print the JSON string representation of the object
print(CreateObjectStorageResponse.to_json())

# convert the object into a dict
create_object_storage_response_dict = create_object_storage_response_instance.to_dict()
# create an instance of CreateObjectStorageResponse from a dict
create_object_storage_response_from_dict = CreateObjectStorageResponse.from_dict(create_object_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


