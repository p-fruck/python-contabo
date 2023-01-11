# CreateObjectStorageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_purchased_space_tb** | **float** | Amount of purchased / requested object storage in TB. | 
**region** | **str** | Region where the object storage should be located. Default is EU. Available regions: EU, US-central, SIN | defaults to "EU"
**auto_scaling** | [**CreateObjectStorageRequestAutoScaling**](CreateObjectStorageRequestAutoScaling.md) |  | [optional] 
**display_name** | **str** | Display name helps to differentiate between object storages, especially if they are in the same region. If display name is not provided, it will be generated. Display name can be changed any time. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


