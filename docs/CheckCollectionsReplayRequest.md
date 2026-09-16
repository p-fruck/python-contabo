# CheckCollectionsReplayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Id of your organization, if unknown please contact us | 
**account_id** | **str** | Account Id | 
**creation_start_time** | **datetime** | Earliest creation date of changes to replay | [optional] 
**creation_end_time** | **datetime** | Latest creation date of changes to replay | [optional] 
**rate** | **float** | Message publishing frequency. How many messages per second get published. Default: 20 | [optional] 
**check_collection_ids** | **List[float]** | Check collection&#39;s id | [optional] 

## Example

```python
from pfruck_contabo.models.check_collections_replay_request import CheckCollectionsReplayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCollectionsReplayRequest from a JSON string
check_collections_replay_request_instance = CheckCollectionsReplayRequest.from_json(json)
# print the JSON string representation of the object
print(CheckCollectionsReplayRequest.to_json())

# convert the object into a dict
check_collections_replay_request_dict = check_collections_replay_request_instance.to_dict()
# create an instance of CheckCollectionsReplayRequest from a dict
check_collections_replay_request_from_dict = CheckCollectionsReplayRequest.from_dict(check_collections_replay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


