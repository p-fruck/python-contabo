# TagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**tag_id** | **int** | Tag&#39;s id | 
**name** | **str** | Tag&#39;s name | 
**color** | **str** | Tag&#39;s color | 

## Example

```python
from pfruck_contabo.models.tag_response import TagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponse from a JSON string
tag_response_instance = TagResponse.from_json(json)
# print the JSON string representation of the object
print(TagResponse.to_json())

# convert the object into a dict
tag_response_dict = tag_response_instance.to_dict()
# create an instance of TagResponse from a dict
tag_response_from_dict = TagResponse.from_dict(tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


