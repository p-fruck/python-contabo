# SupportSignatureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**id** | **str** | HMAC-SHA256 signature of the user id, hex encoded. | 
**validity** | **float** | Signature lifetime in seconds. | 
**timestamp** | **float** | Unix timestamp (seconds) at which the signature expires. Passed to Decagon as the epoch. | 
**system** | **str** | Signing system identifier. | 

## Example

```python
from pfruck_contabo.models.support_signature_response import SupportSignatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportSignatureResponse from a JSON string
support_signature_response_instance = SupportSignatureResponse.from_json(json)
# print the JSON string representation of the object
print(SupportSignatureResponse.to_json())

# convert the object into a dict
support_signature_response_dict = support_signature_response_instance.to_dict()
# create an instance of SupportSignatureResponse from a dict
support_signature_response_from_dict = SupportSignatureResponse.from_dict(support_signature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


