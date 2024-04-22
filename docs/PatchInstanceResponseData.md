# PatchInstanceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | Instance&#39;s id | 
**created_date** | **datetime** | Creation date of the instance | 

## Example

```python
from pfruck_contabo.models.patch_instance_response_data import PatchInstanceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInstanceResponseData from a JSON string
patch_instance_response_data_instance = PatchInstanceResponseData.from_json(json)
# print the JSON string representation of the object
print(PatchInstanceResponseData.to_json())

# convert the object into a dict
patch_instance_response_data_dict = patch_instance_response_data_instance.to_dict()
# create an instance of PatchInstanceResponseData from a dict
patch_instance_response_data_from_dict = PatchInstanceResponseData.from_dict(patch_instance_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


