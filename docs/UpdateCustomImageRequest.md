# UpdateCustomImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Image Name | [optional] 
**description** | **str** | Image Description | [optional] 

## Example

```python
from pfruck_contabo.models.update_custom_image_request import UpdateCustomImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomImageRequest from a JSON string
update_custom_image_request_instance = UpdateCustomImageRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomImageRequest.to_json())

# convert the object into a dict
update_custom_image_request_dict = update_custom_image_request_instance.to_dict()
# create an instance of UpdateCustomImageRequest from a dict
update_custom_image_request_from_dict = UpdateCustomImageRequest.from_dict(update_custom_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


