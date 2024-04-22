# CreateInstanceAddons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_networking** | **object** | Set this attribute if you want to upgrade your instance with the Private Networking addon.   Please provide an empty object for the time being as value. There will be more configuration possible   in the future. | [optional] 
**additional_ips** | **object** | Set this attribute if you want to upgrade your instance with the Additional IPs addon. Please provide an empty object for the time being as value. There will be more configuration possible in the future. | [optional] 
**extra_storage** | [**ExtraStorageRequest**](ExtraStorageRequest.md) | Set this attribute if you want to upgrade your instance with the Extra Storage addon. | [optional] 
**custom_image** | **object** | Set this attribute if you want to upgrade your instance with the Custom Images addon.   Please provide an empty object for the time being as value. There will be more configuration possible   in the future. | [optional] 
**addons_ids** | [**List[AddOnRequest]**](AddOnRequest.md) |  | [optional] 

## Example

```python
from pfruck_contabo.models.create_instance_addons import CreateInstanceAddons

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstanceAddons from a JSON string
create_instance_addons_instance = CreateInstanceAddons.from_json(json)
# print the JSON string representation of the object
print(CreateInstanceAddons.to_json())

# convert the object into a dict
create_instance_addons_dict = create_instance_addons_instance.to_dict()
# create an instance of CreateInstanceAddons from a dict
create_instance_addons_from_dict = CreateInstanceAddons.from_dict(create_instance_addons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


