# PresetRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the preset rule | 
**macro** | **object** | Inbound rules options | 

## Example

```python
from pfruck_contabo.models.preset_rules_response import PresetRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PresetRulesResponse from a JSON string
preset_rules_response_instance = PresetRulesResponse.from_json(json)
# print the JSON string representation of the object
print(PresetRulesResponse.to_json())

# convert the object into a dict
preset_rules_response_dict = preset_rules_response_instance.to_dict()
# create an instance of PresetRulesResponse from a dict
preset_rules_response_from_dict = PresetRulesResponse.from_dict(preset_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


