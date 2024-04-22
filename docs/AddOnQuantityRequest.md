# AddOnQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The number of Addons you wish to aquire. | 

## Example

```python
from pfruck_contabo.models.add_on_quantity_request import AddOnQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnQuantityRequest from a JSON string
add_on_quantity_request_instance = AddOnQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(AddOnQuantityRequest.to_json())

# convert the object into a dict
add_on_quantity_request_dict = add_on_quantity_request_instance.to_dict()
# create an instance of AddOnQuantityRequest from a dict
add_on_quantity_request_from_dict = AddOnQuantityRequest.from_dict(add_on_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


