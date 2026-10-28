# SsoTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**sso_token** | **str** | SSO token UUID used for single sign-on. | 
**url** | **str** | SSO URL to redirect the user to my.contabo.com. | 

## Example

```python
from pfruck_contabo.models.sso_token_response import SsoTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SsoTokenResponse from a JSON string
sso_token_response_instance = SsoTokenResponse.from_json(json)
# print the JSON string representation of the object
print(SsoTokenResponse.to_json())

# convert the object into a dict
sso_token_response_dict = sso_token_response_instance.to_dict()
# create an instance of SsoTokenResponse from a dict
sso_token_response_from_dict = SsoTokenResponse.from_dict(sso_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


