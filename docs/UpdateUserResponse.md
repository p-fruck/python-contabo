# UpdateUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.update_user_response import UpdateUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserResponse from a JSON string
update_user_response_instance = UpdateUserResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateUserResponse.to_json())

# convert the object into a dict
update_user_response_dict = update_user_response_instance.to_dict()
# create an instance of UpdateUserResponse from a dict
update_user_response_from_dict = UpdateUserResponse.from_dict(update_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


