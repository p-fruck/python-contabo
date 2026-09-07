# RulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound** | [**List[FirewallRuleRequest]**](FirewallRuleRequest.md) |  | 

## Example

```python
from pfruck_contabo.models.rules_request import RulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesRequest from a JSON string
rules_request_instance = RulesRequest.from_json(json)
# print the JSON string representation of the object
print(RulesRequest.to_json())

# convert the object into a dict
rules_request_dict = rules_request_instance.to_dict()
# create an instance of RulesRequest from a dict
rules_request_from_dict = RulesRequest.from_dict(rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


