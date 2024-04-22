# FindTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TagResponse]**](TagResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_tag_response import FindTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindTagResponse from a JSON string
find_tag_response_instance = FindTagResponse.from_json(json)
# print the JSON string representation of the object
print(FindTagResponse.to_json())

# convert the object into a dict
find_tag_response_dict = find_tag_response_instance.to_dict()
# create an instance of FindTagResponse from a dict
find_tag_response_from_dict = FindTagResponse.from_dict(find_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


