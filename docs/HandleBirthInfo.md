# HandleBirthInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date | [optional] 
**city** | **str** | City | [optional] 
**zip_code** | **str** | Zipcode | [optional] 
**country** | **str** | Country | [optional] 

## Example

```python
from pfruck_contabo.models.handle_birth_info import HandleBirthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HandleBirthInfo from a JSON string
handle_birth_info_instance = HandleBirthInfo.from_json(json)
# print the JSON string representation of the object
print(HandleBirthInfo.to_json())

# convert the object into a dict
handle_birth_info_dict = handle_birth_info_instance.to_dict()
# create an instance of HandleBirthInfo from a dict
handle_birth_info_from_dict = HandleBirthInfo.from_dict(handle_birth_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


