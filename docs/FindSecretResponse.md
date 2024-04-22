# FindSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SecretResponse]**](SecretResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_secret_response import FindSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindSecretResponse from a JSON string
find_secret_response_instance = FindSecretResponse.from_json(json)
# print the JSON string representation of the object
print(FindSecretResponse.to_json())

# convert the object into a dict
find_secret_response_dict = find_secret_response_instance.to_dict()
# create an instance of FindSecretResponse from a dict
find_secret_response_from_dict = FindSecretResponse.from_dict(find_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


