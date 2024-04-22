# AddOnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the Addon. Please refer to list [here](https://contabo.com/en/product-list/?show_ids&#x3D;true). | 
**quantity** | **int** | The number of Addons you wish to aquire. | 

## Example

```python
from pfruck_contabo.models.add_on_request import AddOnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnRequest from a JSON string
add_on_request_instance = AddOnRequest.from_json(json)
# print the JSON string representation of the object
print(AddOnRequest.to_json())

# convert the object into a dict
add_on_request_dict = add_on_request_instance.to_dict()
# create an instance of AddOnRequest from a dict
add_on_request_from_dict = AddOnRequest.from_dict(add_on_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


