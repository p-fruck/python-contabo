# CreateInstanceAddons


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_networking** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Set this attribute if you want to upgrade your instance with the Private Networking addon.   Please provide an empty object for the time being as value. There will be more configuration possible   in the future. | [optional] 
**additional_ips** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Set this attribute if you want to upgrade your instance with the Additional IPs addon. Please provide an empty object for the time being as value. There will be more configuration possible in the future. | [optional] 
**extra_storage** | [**CreateInstanceAddonsExtraStorage**](CreateInstanceAddonsExtraStorage.md) |  | [optional] 
**custom_image** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Set this attribute if you want to upgrade your instance with the Custom Images addon.   Please provide an empty object for the time being as value. There will be more configuration possible   in the future. | [optional] 
**addons_ids** | [**[AddOnRequest]**](AddOnRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


