# UpdateSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnapshotResponse]**](SnapshotResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.update_snapshot_response import UpdateSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotResponse from a JSON string
update_snapshot_response_instance = UpdateSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotResponse.to_json())

# convert the object into a dict
update_snapshot_response_dict = update_snapshot_response_instance.to_dict()
# create an instance of UpdateSnapshotResponse from a dict
update_snapshot_response_from_dict = UpdateSnapshotResponse.from_dict(update_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


