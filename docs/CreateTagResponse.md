# CreateTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateTagResponseData]**](CreateTagResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_tag_response import CreateTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagResponse from a JSON string
create_tag_response_instance = CreateTagResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTagResponse.to_json())

# convert the object into a dict
create_tag_response_dict = create_tag_response_instance.to_dict()
# create an instance of CreateTagResponse from a dict
create_tag_response_from_dict = CreateTagResponse.from_dict(create_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


