# HandlePhone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | prefix | 
**number** | **str** | number | 

## Example

```python
from pfruck_contabo.models.handle_phone import HandlePhone

# TODO update the JSON string below
json = "{}"
# create an instance of HandlePhone from a JSON string
handle_phone_instance = HandlePhone.from_json(json)
# print the JSON string representation of the object
print(HandlePhone.to_json())

# convert the object into a dict
handle_phone_dict = handle_phone_instance.to_dict()
# create an instance of HandlePhone from a dict
handle_phone_from_dict = HandlePhone.from_dict(handle_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


