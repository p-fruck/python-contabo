# FindSsoTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SsoTokenResponse]**](SsoTokenResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_sso_token_response import FindSsoTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindSsoTokenResponse from a JSON string
find_sso_token_response_instance = FindSsoTokenResponse.from_json(json)
# print the JSON string representation of the object
print(FindSsoTokenResponse.to_json())

# convert the object into a dict
find_sso_token_response_dict = find_sso_token_response_instance.to_dict()
# create an instance of FindSsoTokenResponse from a dict
find_sso_token_response_from_dict = FindSsoTokenResponse.from_dict(find_sso_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


