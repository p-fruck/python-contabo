# CreateCustomImageFailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Unsupported Media Type: Please provide a direct link to an .iso or .qcow2 image. | 
**status_code** | **int** | statuscode:415 | 

## Example

```python
from pfruck_contabo.models.create_custom_image_fail_response import CreateCustomImageFailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomImageFailResponse from a JSON string
create_custom_image_fail_response_instance = CreateCustomImageFailResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCustomImageFailResponse.to_json())

# convert the object into a dict
create_custom_image_fail_response_dict = create_custom_image_fail_response_instance.to_dict()
# create an instance of CreateCustomImageFailResponse from a dict
create_custom_image_fail_response_from_dict = CreateCustomImageFailResponse.from_dict(create_custom_image_fail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


