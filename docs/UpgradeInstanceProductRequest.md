# UpgradeInstanceProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** | ID of the upgrade offer as provided by the upgrade options. | 
**provisioning_type** | **str** | Provisioning type for the upgrade. Use &#x60;installation&#x60; for a fresh installation or &#x60;migration&#x60; to keep the instance&#39;s existing data. | 
**image_id** | **str** | ImageId of the image to install (only in case of &#x60;installation&#x60;). | [optional] 
**application_id** | **str** | ApplicationId of the panel to install (only in case of &#x60;installation&#x60;). | [optional] 
**storage_addon** | **bool** | Set to true to keep the storage extension addon (only for SSD and NVMe). | [optional] 
**remarks** | **str** | Customer remarks for the upgrade. | [optional] 

## Example

```python
from pfruck_contabo.models.upgrade_instance_product_request import UpgradeInstanceProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeInstanceProductRequest from a JSON string
upgrade_instance_product_request_instance = UpgradeInstanceProductRequest.from_json(json)
# print the JSON string representation of the object
print(UpgradeInstanceProductRequest.to_json())

# convert the object into a dict
upgrade_instance_product_request_dict = upgrade_instance_product_request_instance.to_dict()
# create an instance of UpgradeInstanceProductRequest from a dict
upgrade_instance_product_request_from_dict = UpgradeInstanceProductRequest.from_dict(upgrade_instance_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


