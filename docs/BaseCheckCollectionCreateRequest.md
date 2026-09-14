# BaseCheckCollectionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**check_collection_template_id** | **float** | Check Template for this check collection | 

## Example

```python
from pfruck_contabo.models.base_check_collection_create_request import BaseCheckCollectionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCheckCollectionCreateRequest from a JSON string
base_check_collection_create_request_instance = BaseCheckCollectionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BaseCheckCollectionCreateRequest.to_json())

# convert the object into a dict
base_check_collection_create_request_dict = base_check_collection_create_request_instance.to_dict()
# create an instance of BaseCheckCollectionCreateRequest from a dict
base_check_collection_create_request_from_dict = BaseCheckCollectionCreateRequest.from_dict(base_check_collection_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


