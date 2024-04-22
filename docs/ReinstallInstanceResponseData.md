# ReinstallInstanceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | Instance&#39;s id | 
**created_date** | **datetime** | Creation date for instance | 

## Example

```python
from pfruck_contabo.models.reinstall_instance_response_data import ReinstallInstanceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReinstallInstanceResponseData from a JSON string
reinstall_instance_response_data_instance = ReinstallInstanceResponseData.from_json(json)
# print the JSON string representation of the object
print(ReinstallInstanceResponseData.to_json())

# convert the object into a dict
reinstall_instance_response_data_dict = reinstall_instance_response_data_instance.to_dict()
# create an instance of ReinstallInstanceResponseData from a dict
reinstall_instance_response_data_from_dict = ReinstallInstanceResponseData.from_dict(reinstall_instance_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


