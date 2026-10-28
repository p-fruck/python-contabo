# ListInstanceProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceProduct]**](InstanceProduct.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.list_instance_products_response import ListInstanceProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInstanceProductsResponse from a JSON string
list_instance_products_response_instance = ListInstanceProductsResponse.from_json(json)
# print the JSON string representation of the object
print(ListInstanceProductsResponse.to_json())

# convert the object into a dict
list_instance_products_response_dict = list_instance_products_response_instance.to_dict()
# create an instance of ListInstanceProductsResponse from a dict
list_instance_products_response_from_dict = ListInstanceProductsResponse.from_dict(list_instance_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


