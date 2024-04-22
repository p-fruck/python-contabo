# ListSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[SnapshotResponse]**](SnapshotResponse.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.list_snapshot_response import ListSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotResponse from a JSON string
list_snapshot_response_instance = ListSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotResponse.to_json())

# convert the object into a dict
list_snapshot_response_dict = list_snapshot_response_instance.to_dict()
# create an instance of ListSnapshotResponse from a dict
list_snapshot_response_from_dict = ListSnapshotResponse.from_dict(list_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


