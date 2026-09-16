# BaseRemedyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**remedy_template_id** | **float** | Remedy Template for this remedy | 
**remedy_collection_id** | **float** | Remedy Collection for this remedy | [optional] 

## Example

```python
from pfruck_contabo.models.base_remedy_create_request import BaseRemedyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRemedyCreateRequest from a JSON string
base_remedy_create_request_instance = BaseRemedyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BaseRemedyCreateRequest.to_json())

# convert the object into a dict
base_remedy_create_request_dict = base_remedy_create_request_instance.to_dict()
# create an instance of BaseRemedyCreateRequest from a dict
base_remedy_create_request_from_dict = BaseRemedyCreateRequest.from_dict(base_remedy_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


