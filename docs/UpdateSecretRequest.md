# UpdateSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret to be saved | [optional] 
**value** | **str** | The value of the secret to be saved | [optional] 

## Example

```python
from pfruck_contabo.models.update_secret_request import UpdateSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecretRequest from a JSON string
update_secret_request_instance = UpdateSecretRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSecretRequest.to_json())

# convert the object into a dict
update_secret_request_dict = update_secret_request_instance.to_dict()
# create an instance of UpdateSecretRequest from a dict
update_secret_request_from_dict = UpdateSecretRequest.from_dict(update_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


