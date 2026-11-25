# DomainAuthCodeRegenerateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DomainAuthCodeResponse]**](DomainAuthCodeResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.domain_auth_code_regenerate_response import DomainAuthCodeRegenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAuthCodeRegenerateResponse from a JSON string
domain_auth_code_regenerate_response_instance = DomainAuthCodeRegenerateResponse.from_json(json)
# print the JSON string representation of the object
print(DomainAuthCodeRegenerateResponse.to_json())

# convert the object into a dict
domain_auth_code_regenerate_response_dict = domain_auth_code_regenerate_response_instance.to_dict()
# create an instance of DomainAuthCodeRegenerateResponse from a dict
domain_auth_code_regenerate_response_from_dict = DomainAuthCodeRegenerateResponse.from_dict(domain_auth_code_regenerate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


