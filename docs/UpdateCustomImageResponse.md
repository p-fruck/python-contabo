# UpdateCustomImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UpdateCustomImageResponseData]**](UpdateCustomImageResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.update_custom_image_response import UpdateCustomImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomImageResponse from a JSON string
update_custom_image_response_instance = UpdateCustomImageResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomImageResponse.to_json())

# convert the object into a dict
update_custom_image_response_dict = update_custom_image_response_instance.to_dict()
# create an instance of UpdateCustomImageResponse from a dict
update_custom_image_response_from_dict = UpdateCustomImageResponse.from_dict(update_custom_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


