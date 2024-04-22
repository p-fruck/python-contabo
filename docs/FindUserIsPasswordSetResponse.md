# FindUserIsPasswordSetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserIsPasswordSetResponse]**](UserIsPasswordSetResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_user_is_password_set_response import FindUserIsPasswordSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindUserIsPasswordSetResponse from a JSON string
find_user_is_password_set_response_instance = FindUserIsPasswordSetResponse.from_json(json)
# print the JSON string representation of the object
print(FindUserIsPasswordSetResponse.to_json())

# convert the object into a dict
find_user_is_password_set_response_dict = find_user_is_password_set_response_instance.to_dict()
# create an instance of FindUserIsPasswordSetResponse from a dict
find_user_is_password_set_response_from_dict = FindUserIsPasswordSetResponse.from_dict(find_user_is_password_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


