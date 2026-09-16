# ListPresetRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PresetRulesResponse]**](PresetRulesResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.list_preset_rules_response import ListPresetRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPresetRulesResponse from a JSON string
list_preset_rules_response_instance = ListPresetRulesResponse.from_json(json)
# print the JSON string representation of the object
print(ListPresetRulesResponse.to_json())

# convert the object into a dict
list_preset_rules_response_dict = list_preset_rules_response_instance.to_dict()
# create an instance of ListPresetRulesResponse from a dict
list_preset_rules_response_from_dict = ListPresetRulesResponse.from_dict(list_preset_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


