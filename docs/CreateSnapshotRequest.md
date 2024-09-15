# CreateSnapshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the snapshot. It may contain letters, numbers, spaces, dashes. There is a limit of 30 characters per snapshot. | 
**description** | **str** | The description of the snapshot. There is a limit of 255 characters per snapshot. | [optional] 

## Example

```python
from pfruck_contabo.models.create_snapshot_request import CreateSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotRequest from a JSON string
create_snapshot_request_instance = CreateSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotRequest.to_json())

# convert the object into a dict
create_snapshot_request_dict = create_snapshot_request_instance.to_dict()
# create an instance of CreateSnapshotRequest from a dict
create_snapshot_request_from_dict = CreateSnapshotRequest.from_dict(create_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


