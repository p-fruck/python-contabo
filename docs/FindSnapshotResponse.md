# FindSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnapshotResponse]**](SnapshotResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_snapshot_response import FindSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindSnapshotResponse from a JSON string
find_snapshot_response_instance = FindSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(FindSnapshotResponse.to_json())

# convert the object into a dict
find_snapshot_response_dict = find_snapshot_response_instance.to_dict()
# create an instance of FindSnapshotResponse from a dict
find_snapshot_response_from_dict = FindSnapshotResponse.from_dict(find_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


