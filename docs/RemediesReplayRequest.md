# RemediesReplayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Id of your organization, if unknown please contact us | 
**account_id** | **str** | Account Id | 
**creation_start_time** | **datetime** | Earliest creation date of changes to replay | [optional] 
**creation_end_time** | **datetime** | Latest creation date of changes to replay | [optional] 
**rate** | **float** | Message publishing frequency. How many messages per second get published. Default: 20 | [optional] 
**remedy_ids** | **List[float]** | Remedy&#39;s id | [optional] 

## Example

```python
from pfruck_contabo.models.remedies_replay_request import RemediesReplayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemediesReplayRequest from a JSON string
remedies_replay_request_instance = RemediesReplayRequest.from_json(json)
# print the JSON string representation of the object
print(RemediesReplayRequest.to_json())

# convert the object into a dict
remedies_replay_request_dict = remedies_replay_request_instance.to_dict()
# create an instance of RemediesReplayRequest from a dict
remedies_replay_request_from_dict = RemediesReplayRequest.from_dict(remedies_replay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


