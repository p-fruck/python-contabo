# CreateObjectStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | Region where the object storage should be located. Default is EU. Available regions: EU, US-central, SIN | [default to 'EU']
**auto_scaling** | [**AutoScalingTypeRequest**](AutoScalingTypeRequest.md) | Autoscaling settings | [optional] 
**total_purchased_space_tb** | **float** | Amount of purchased / requested object storage in TB. | 
**display_name** | **str** | Display name helps to differentiate between object storages, especially if they are in the same region. If display name is not provided, it will be generated. Display name can be changed any time. | [optional] 

## Example

```python
from pfruck_contabo.models.create_object_storage_request import CreateObjectStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectStorageRequest from a JSON string
create_object_storage_request_instance = CreateObjectStorageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateObjectStorageRequest.to_json())

# convert the object into a dict
create_object_storage_request_dict = create_object_storage_request_instance.to_dict()
# create an instance of CreateObjectStorageRequest from a dict
create_object_storage_request_from_dict = CreateObjectStorageRequest.from_dict(create_object_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


