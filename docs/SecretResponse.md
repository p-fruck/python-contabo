# SecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your Customer number | 
**secret_id** | **float** | Secret&#39;s id | 
**name** | **str** | The name assigned to the password/ssh | 
**type** | **str** | The type of the secret. This will be available only when retrieving secrets | 
**value** | **str** | The value of the secret. This will be available only when retrieving a single secret | 
**created_at** | **datetime** | The creation date for the secret | 
**updated_at** | **datetime** | The last update date for the secret | 

## Example

```python
from pfruck_contabo.models.secret_response import SecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretResponse from a JSON string
secret_response_instance = SecretResponse.from_json(json)
# print the JSON string representation of the object
print(SecretResponse.to_json())

# convert the object into a dict
secret_response_dict = secret_response_instance.to_dict()
# create an instance of SecretResponse from a dict
secret_response_from_dict = SecretResponse.from_dict(secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


