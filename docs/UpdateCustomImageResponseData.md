# UpdateCustomImageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**image_id** | **str** | Image&#39;s id | 

## Example

```python
from pfruck_contabo.models.update_custom_image_response_data import UpdateCustomImageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomImageResponseData from a JSON string
update_custom_image_response_data_instance = UpdateCustomImageResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomImageResponseData.to_json())

# convert the object into a dict
update_custom_image_response_data_dict = update_custom_image_response_data_instance.to_dict()
# create an instance of UpdateCustomImageResponseData from a dict
update_custom_image_response_data_from_dict = UpdateCustomImageResponseData.from_dict(update_custom_image_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


