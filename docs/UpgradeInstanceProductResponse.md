# UpgradeInstanceProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UpgradeInstanceProductData]**](UpgradeInstanceProductData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.upgrade_instance_product_response import UpgradeInstanceProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeInstanceProductResponse from a JSON string
upgrade_instance_product_response_instance = UpgradeInstanceProductResponse.from_json(json)
# print the JSON string representation of the object
print(UpgradeInstanceProductResponse.to_json())

# convert the object into a dict
upgrade_instance_product_response_dict = upgrade_instance_product_response_instance.to_dict()
# create an instance of UpgradeInstanceProductResponse from a dict
upgrade_instance_product_response_from_dict = UpgradeInstanceProductResponse.from_dict(upgrade_instance_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


