# RemediesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**remedy_template_id** | **float** | Remedy Template for this remedy | 
**remedy_collection_id** | **float** | Remedy Collection for this remedy | [optional] 
**org_id** | **str** | Id of your organization, if unknown please contact us | 
**account_id** | **str** | Account Id | 

## Example

```python
from pfruck_contabo.models.remedies_create_request import RemediesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemediesCreateRequest from a JSON string
remedies_create_request_instance = RemediesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RemediesCreateRequest.to_json())

# convert the object into a dict
remedies_create_request_dict = remedies_create_request_instance.to_dict()
# create an instance of RemediesCreateRequest from a dict
remedies_create_request_from_dict = RemediesCreateRequest.from_dict(remedies_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


