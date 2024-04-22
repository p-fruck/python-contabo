# GenerateClientSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientSecretResponse]**](ClientSecretResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.generate_client_secret_response import GenerateClientSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateClientSecretResponse from a JSON string
generate_client_secret_response_instance = GenerateClientSecretResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateClientSecretResponse.to_json())

# convert the object into a dict
generate_client_secret_response_dict = generate_client_secret_response_instance.to_dict()
# create an instance of GenerateClientSecretResponse from a dict
generate_client_secret_response_from_dict = GenerateClientSecretResponse.from_dict(generate_client_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


