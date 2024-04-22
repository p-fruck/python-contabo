# CreateCustomImageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**image_id** | **str** | Image&#39;s id | 

## Example

```python
from pfruck_contabo.models.create_custom_image_response_data import CreateCustomImageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomImageResponseData from a JSON string
create_custom_image_response_data_instance = CreateCustomImageResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateCustomImageResponseData.to_json())

# convert the object into a dict
create_custom_image_response_data_dict = create_custom_image_response_data_instance.to_dict()
# create an instance of CreateCustomImageResponseData from a dict
create_custom_image_response_data_from_dict = CreateCustomImageResponseData.from_dict(create_custom_image_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


