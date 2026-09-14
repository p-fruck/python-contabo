# BaseCheckCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Object type to be handled | 
**object_id** | **str** | ID of the object, to be handled | 
**check_template_id** | **float** | Check Template for this check | 
**check_collection_id** | **float** | Check Collection for this check | [optional] 

## Example

```python
from pfruck_contabo.models.base_check_create_request import BaseCheckCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCheckCreateRequest from a JSON string
base_check_create_request_instance = BaseCheckCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BaseCheckCreateRequest.to_json())

# convert the object into a dict
base_check_create_request_dict = base_check_create_request_instance.to_dict()
# create an instance of BaseCheckCreateRequest from a dict
base_check_create_request_from_dict = BaseCheckCreateRequest.from_dict(base_check_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


