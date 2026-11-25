# Changes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | **object** | Previous values of changed properties | 
**new** | **object** | New values of changed properties | 

## Example

```python
from pfruck_contabo.models.changes import Changes

# TODO update the JSON string below
json = "{}"
# create an instance of Changes from a JSON string
changes_instance = Changes.from_json(json)
# print the JSON string representation of the object
print(Changes.to_json())

# convert the object into a dict
changes_dict = changes_instance.to_dict()
# create an instance of Changes from a dict
changes_from_dict = Changes.from_dict(changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


