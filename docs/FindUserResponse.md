# FindUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserResponse]**](UserResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_user_response import FindUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindUserResponse from a JSON string
find_user_response_instance = FindUserResponse.from_json(json)
# print the JSON string representation of the object
print(FindUserResponse.to_json())

# convert the object into a dict
find_user_response_dict = find_user_response_instance.to_dict()
# create an instance of FindUserResponse from a dict
find_user_response_from_dict = FindUserResponse.from_dict(find_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


