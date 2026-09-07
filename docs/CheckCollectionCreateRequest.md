# CheckCollectionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**check_collection_template_id** | **float** | Check Template for this check collection | 
**org_id** | **str** | Id of your organization, if unknown please contact us | 
**account_id** | **str** | Account Id | 

## Example

```python
from pfruck_contabo.models.check_collection_create_request import CheckCollectionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionCreateRequest from a JSON string
check_collection_create_request_instance = CheckCollectionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionCreateRequest.to_json())

# convert the object into a dict
check_collection_create_request_dict = check_collection_create_request_instance.to_dict()
# create an instance of CheckCollectionCreateRequest from a dict
check_collection_create_request_from_dict = CheckCollectionCreateRequest.from_dict(check_collection_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


