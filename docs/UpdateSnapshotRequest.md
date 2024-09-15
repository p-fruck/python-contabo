# UpdateSnapshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the snapshot. Tags may contain only letters, numbers, spaces, dashes. There is a limit of 30 characters per snapshot. | [optional] 
**description** | **str** | The description of the snapshot. There is a limit of 255 characters per snapshot. | [optional] 

## Example

```python
from pfruck_contabo.models.update_snapshot_request import UpdateSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotRequest from a JSON string
update_snapshot_request_instance = UpdateSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotRequest.to_json())

# convert the object into a dict
update_snapshot_request_dict = update_snapshot_request_instance.to_dict()
# create an instance of UpdateSnapshotRequest from a dict
update_snapshot_request_from_dict = UpdateSnapshotRequest.from_dict(update_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


