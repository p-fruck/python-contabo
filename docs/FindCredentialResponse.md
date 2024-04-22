# FindCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CredentialData]**](CredentialData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_credential_response import FindCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindCredentialResponse from a JSON string
find_credential_response_instance = FindCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(FindCredentialResponse.to_json())

# convert the object into a dict
find_credential_response_dict = find_credential_response_instance.to_dict()
# create an instance of FindCredentialResponse from a dict
find_credential_response_from_dict = FindCredentialResponse.from_dict(find_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


