# CredentialData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**access_key** | **str** | Access key ID. | 
**secret_key** | **str** | Secret key ID. | 
**object_storage_id** | **str** | Object Storage ID. | 
**display_name** | **str** | Object Storage Name. | 
**region** | **str** | Object Storage Region. | 
**credential_id** | **float** | Object Storage Credential ID | 

## Example

```python
from pfruck_contabo.models.credential_data import CredentialData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialData from a JSON string
credential_data_instance = CredentialData.from_json(json)
# print the JSON string representation of the object
print(CredentialData.to_json())

# convert the object into a dict
credential_data_dict = credential_data_instance.to_dict()
# create an instance of CredentialData from a dict
credential_data_from_dict = CredentialData.from_dict(credential_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


