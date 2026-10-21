# ChecksReplayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Id of your organization, if unknown please contact us | 
**account_id** | **str** | Account Id | 
**creation_start_time** | **datetime** | Earliest creation date of changes to replay | [optional] 
**creation_end_time** | **datetime** | Latest creation date of changes to replay | [optional] 
**rate** | **float** | Message publishing frequency. How many messages per second get published. Default: 20 | [optional] 
**check_ids** | **List[float]** | Check&#39;s id | [optional] 

## Example

```python
from pfruck_contabo.models.checks_replay_request import ChecksReplayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksReplayRequest from a JSON string
checks_replay_request_instance = ChecksReplayRequest.from_json(json)
# print the JSON string representation of the object
print(ChecksReplayRequest.to_json())

# convert the object into a dict
checks_replay_request_dict = checks_replay_request_instance.to_dict()
# create an instance of ChecksReplayRequest from a dict
checks_replay_request_from_dict = ChecksReplayRequest.from_dict(checks_replay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


