# ReplayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditCountResponse]**](AuditCountResponse.md) |  | 

## Example

```python
from pfruck_contabo.models.replay_response import ReplayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayResponse from a JSON string
replay_response_instance = ReplayResponse.from_json(json)
# print the JSON string representation of the object
print(ReplayResponse.to_json())

# convert the object into a dict
replay_response_dict = replay_response_instance.to_dict()
# create an instance of ReplayResponse from a dict
replay_response_from_dict = ReplayResponse.from_dict(replay_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


