# FindSupportSignatureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SupportSignatureResponse]**](SupportSignatureResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_support_signature_response import FindSupportSignatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindSupportSignatureResponse from a JSON string
find_support_signature_response_instance = FindSupportSignatureResponse.from_json(json)
# print the JSON string representation of the object
print(FindSupportSignatureResponse.to_json())

# convert the object into a dict
find_support_signature_response_dict = find_support_signature_response_instance.to_dict()
# create an instance of FindSupportSignatureResponse from a dict
find_support_signature_response_from_dict = FindSupportSignatureResponse.from_dict(find_support_signature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


