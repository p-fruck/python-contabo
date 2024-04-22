# CreateSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SecretResponse]**](SecretResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_secret_response import CreateSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretResponse from a JSON string
create_secret_response_instance = CreateSecretResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSecretResponse.to_json())

# convert the object into a dict
create_secret_response_dict = create_secret_response_instance.to_dict()
# create an instance of CreateSecretResponse from a dict
create_secret_response_from_dict = CreateSecretResponse.from_dict(create_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


