# CreateSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret that will keep the password | 
**value** | **str** | The secret value that needs to be saved. In case of a password it must match a pattern with at least one upper and lower case character and either one number with two special characters &#x60;!@#$^&amp;*?_~&#x60; or at least three numbers with one special character &#x60;!@#$^&amp;*?_~&#x60;. This is expressed in the following regular expression: &#x60;^((?&#x3D;.*?[A-Z]{1,})(?&#x3D;.*?[a-z]{1,}))(((?&#x3D;(?:[^d]*d){1})(?&#x3D;([^^&amp;*?_~]*[!@#$^&amp;*?_~]){2,}))|((?&#x3D;(?:[^d]*d){3})(?&#x3D;.*?[!@#$^&amp;*?_~]+))).{8,}$&#x60; | 
**type** | **str** | The type of the secret. Can be &#x60;password&#x60; or &#x60;ssh&#x60; | 

## Example

```python
from pfruck_contabo.models.create_secret_request import CreateSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretRequest from a JSON string
create_secret_request_instance = CreateSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSecretRequest.to_json())

# convert the object into a dict
create_secret_request_dict = create_secret_request_instance.to_dict()
# create an instance of CreateSecretRequest from a dict
create_secret_request_from_dict = CreateSecretRequest.from_dict(create_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


