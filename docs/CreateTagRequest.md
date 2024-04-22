# CreateTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tag. Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag. | 
**color** | **str** | The color of the tag. Color can be specified using hexadecimal value. Default color is #0A78C3 | [default to '#0A78C3']

## Example

```python
from pfruck_contabo.models.create_tag_request import CreateTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagRequest from a JSON string
create_tag_request_instance = CreateTagRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTagRequest.to_json())

# convert the object into a dict
create_tag_request_dict = create_tag_request_instance.to_dict()
# create an instance of CreateTagRequest from a dict
create_tag_request_from_dict = CreateTagRequest.from_dict(create_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


