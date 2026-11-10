# ChangedAuthCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **bool** | Flag that indicates if the auth code got changed | [optional] 
**var_date** | **datetime** | The date when auth code got changed | [optional] 

## Example

```python
from pfruck_contabo.models.changed_auth_code import ChangedAuthCode

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedAuthCode from a JSON string
changed_auth_code_instance = ChangedAuthCode.from_json(json)
# print the JSON string representation of the object
print(ChangedAuthCode.to_json())

# convert the object into a dict
changed_auth_code_dict = changed_auth_code_instance.to_dict()
# create an instance of ChangedAuthCode from a dict
changed_auth_code_from_dict = ChangedAuthCode.from_dict(changed_auth_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


