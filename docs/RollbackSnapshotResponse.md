# RollbackSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) | Links for easy navigation. | 

## Example

```python
from pfruck_contabo.models.rollback_snapshot_response import RollbackSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSnapshotResponse from a JSON string
rollback_snapshot_response_instance = RollbackSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(RollbackSnapshotResponse.to_json())

# convert the object into a dict
rollback_snapshot_response_dict = rollback_snapshot_response_instance.to_dict()
# create an instance of RollbackSnapshotResponse from a dict
rollback_snapshot_response_from_dict = RollbackSnapshotResponse.from_dict(rollback_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


