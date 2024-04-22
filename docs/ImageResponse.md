# ImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | Image&#39;s id | 
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Customer ID | 
**name** | **str** | Image Name | 
**description** | **str** | Image Description | 
**url** | **str** | URL from where the image has been downloaded / provided. | 
**size_mb** | **float** | Image Size in MB | 
**uploaded_size_mb** | **float** | Image Uploaded Size in MB | 
**os_type** | **str** | Type of operating system (OS) | 
**version** | **str** | Version number to distinguish the contents of an image. Could be the version of the operating system for example. | 
**format** | **str** | Image format | 
**status** | **str** | Image status (e.g. if image is still downloading) | 
**error_message** | **str** | Image download error message | 
**standard_image** | **bool** | Flag indicating that image is either a standard (true) or a custom image (false) | 
**creation_date** | **datetime** | The creation date time for the image | 
**last_modified_date** | **datetime** | The last modified date time for the image | 

## Example

```python
from pfruck_contabo.models.image_response import ImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResponse from a JSON string
image_response_instance = ImageResponse.from_json(json)
# print the JSON string representation of the object
print(ImageResponse.to_json())

# convert the object into a dict
image_response_dict = image_response_instance.to_dict()
# create an instance of ImageResponse from a dict
image_response_from_dict = ImageResponse.from_dict(image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


