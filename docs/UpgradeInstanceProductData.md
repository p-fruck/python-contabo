# UpgradeInstanceProductData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | The identifier of the instance | 
**ticket_number** | **str** | Support ticket number created for the upgrade | 
**automatic** | **bool** | Indicates whether the upgrade will be processed automatically or manually. | 

## Example

```python
from pfruck_contabo.models.upgrade_instance_product_data import UpgradeInstanceProductData

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeInstanceProductData from a JSON string
upgrade_instance_product_data_instance = UpgradeInstanceProductData.from_json(json)
# print the JSON string representation of the object
print(UpgradeInstanceProductData.to_json())

# convert the object into a dict
upgrade_instance_product_data_dict = upgrade_instance_product_data_instance.to_dict()
# create an instance of UpgradeInstanceProductData from a dict
upgrade_instance_product_data_from_dict = UpgradeInstanceProductData.from_dict(upgrade_instance_product_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


