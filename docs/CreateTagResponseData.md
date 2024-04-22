# CreateTagResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**tag_id** | **int** | Tag&#39;s id | 

## Example

```python
from pfruck_contabo.models.create_tag_response_data import CreateTagResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagResponseData from a JSON string
create_tag_response_data_instance = CreateTagResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateTagResponseData.to_json())

# convert the object into a dict
create_tag_response_data_dict = create_tag_response_data_instance.to_dict()
# create an instance of CreateTagResponseData from a dict
create_tag_response_data_from_dict = CreateTagResponseData.from_dict(create_tag_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


