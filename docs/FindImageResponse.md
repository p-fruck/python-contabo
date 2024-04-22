# FindImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ImageResponse]**](ImageResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_image_response import FindImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindImageResponse from a JSON string
find_image_response_instance = FindImageResponse.from_json(json)
# print the JSON string representation of the object
print(FindImageResponse.to_json())

# convert the object into a dict
find_image_response_dict = find_image_response_instance.to_dict()
# create an instance of FindImageResponse from a dict
find_image_response_from_dict = FindImageResponse.from_dict(find_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


