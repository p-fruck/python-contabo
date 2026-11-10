# InstanceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant id | 
**customer_id** | **str** | Customer ID | 
**instance_id** | **int** | Instance ID | 
**product_id** | **str** | Product ID | 
**name** | **str** | Product name | 
**frontend_name** | **str** | Short product name intended for display in the frontend. Falls back to the full product name if no dedicated frontend name is defined. | [optional] 
**category** | **str** | Instance&#39;s category depending on Product Id | 
**ram_size_gb** | **float** | RAM size in GB | 
**disk_size_gb** | **float** | Disk size in GB | 
**cpu_cores** | **int** | CPU core count | 
**net_speed** | **int** | Network speed in Mbit/s | 
**snapshots** | **int** | Number of snapshots included in the product | 
**vs_price** | **float** | Base virtual server price | 
**windows_price** | **float** | Additional price for Windows licensing | 
**backup_price** | **float** | Price for automated backup service | 
**storage_extension_price** | **float** | Price for storage extension add-on | 
**location_fee_price** | **float** | Additional fee applied for specific datacenter locations | 
**addons_price** | **float** | Aggregated price for all active add-ons | 
**has_storage_extension** | **bool** | Indicates whether a storage extension is attached | 
**has_backup_addon** | **bool** | Indicates whether the automated backup add-on is attached | [optional] 
**has_windows** | **bool** | Indicates whether the Windows add-on is attached | [optional] 
**has_location_fee** | **bool** | Indicates whether a location fee add-on is attached | [optional] 
**current** | **bool** | True if this product entry reflects the currently active subscription for the instance | 
**offer_id** | **int** | Identifier of the upgrade offer. Provide it as &#x60;offerId&#x60; when submitting the upgrade. Not set on the currently assigned product. | [optional] 
**location_change_required** | **bool** | The offer is not available at the current location | [optional] 
**live_migration_available** | **bool** | The upgrade can be performed while keeping the existing data (&#x60;migration&#x60; provisioning type) | [optional] 
**live_migration_disabled_reason** | **str** | Reason why the existing data cannot be kept for this offer. Not set when it can be kept. | [optional] 
**storage_extension_available** | **bool** | The storage extension add-on can be selected for this offer | [optional] 
**backup_available** | **bool** | The automated backup add-on can be selected for this offer | [optional] 
**upgrade_discount** | **int** | Upgrade discount percentage applied to this offer | [optional] 
**vs_original_price** | **float** | Original gross price without add-ons and before the upgrade discount | [optional] 
**required_confirmations** | **List[str]** | Confirmations the customer has to accept for this offer | [optional] 
**price_difference_with_storage_extension** | **float** | Price difference charged when the storage extension is selected | [optional] 
**price_difference_without_storage_extension** | **float** | Price difference charged when the storage extension is not selected | [optional] 

## Example

```python
from pfruck_contabo.models.instance_product import InstanceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceProduct from a JSON string
instance_product_instance = InstanceProduct.from_json(json)
# print the JSON string representation of the object
print(InstanceProduct.to_json())

# convert the object into a dict
instance_product_dict = instance_product_instance.to_dict()
# create an instance of InstanceProduct from a dict
instance_product_from_dict = InstanceProduct.from_dict(instance_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


