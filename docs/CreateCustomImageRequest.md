# CreateCustomImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Image Name | 
**description** | **str** | Image Description | [optional] 
**url** | **str** | URL from where the image has been downloaded / provided. | 
**os_type** | **str** | Provided type of operating system (OS). Please specify &#x60;Windows&#x60; for MS Windows and &#x60;Linux&#x60; for other OS. Specifying wrong OS type may lead to disfunctional cloud instance. | 
**version** | **str** | Version number to distinguish the contents of an image. Could be the version of the operating system for example. | 

## Example

```python
from pfruck_contabo.models.create_custom_image_request import CreateCustomImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomImageRequest from a JSON string
create_custom_image_request_instance = CreateCustomImageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomImageRequest.to_json())

# convert the object into a dict
create_custom_image_request_dict = create_custom_image_request_instance.to_dict()
# create an instance of CreateCustomImageRequest from a dict
create_custom_image_request_from_dict = CreateCustomImageRequest.from_dict(create_custom_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


