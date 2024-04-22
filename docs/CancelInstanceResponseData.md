# CancelInstanceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**instance_id** | **int** | Instance&#39;s id | 
**cancel_date** | **date** | The date on which the instance will be cancelled | 

## Example

```python
from pfruck_contabo.models.cancel_instance_response_data import CancelInstanceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CancelInstanceResponseData from a JSON string
cancel_instance_response_data_instance = CancelInstanceResponseData.from_json(json)
# print the JSON string representation of the object
print(CancelInstanceResponseData.to_json())

# convert the object into a dict
cancel_instance_response_data_dict = cancel_instance_response_data_instance.to_dict()
# create an instance of CancelInstanceResponseData from a dict
cancel_instance_response_data_from_dict = CancelInstanceResponseData.from_dict(cancel_instance_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


