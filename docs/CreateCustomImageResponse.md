# CreateCustomImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateCustomImageResponseData]**](CreateCustomImageResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_custom_image_response import CreateCustomImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomImageResponse from a JSON string
create_custom_image_response_instance = CreateCustomImageResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCustomImageResponse.to_json())

# convert the object into a dict
create_custom_image_response_dict = create_custom_image_response_instance.to_dict()
# create an instance of CreateCustomImageResponse from a dict
create_custom_image_response_from_dict = CreateCustomImageResponse.from_dict(create_custom_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


