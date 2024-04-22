# SnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**snapshot_id** | **str** | Snapshot&#39;s id | 
**name** | **str** | The name of the snapshot. | 
**description** | **str** | The description of the snapshot. | 
**instance_id** | **int** | The instance identifier associated with the snapshot | 
**created_date** | **datetime** | The date when the snapshot was created | 
**auto_delete_date** | **datetime** | The date when the snapshot will be auto-deleted | 
**image_id** | **str** | Image Id the snapshot was taken on | 
**image_name** | **str** | Image name the snapshot was taken on | 

## Example

```python
from pfruck_contabo.models.snapshot_response import SnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResponse from a JSON string
snapshot_response_instance = SnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotResponse.to_json())

# convert the object into a dict
snapshot_response_dict = snapshot_response_instance.to_dict()
# create an instance of SnapshotResponse from a dict
snapshot_response_from_dict = SnapshotResponse.from_dict(snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


