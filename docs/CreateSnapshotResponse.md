# CreateSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SnapshotResponse]**](SnapshotResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_snapshot_response import CreateSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotResponse from a JSON string
create_snapshot_response_instance = CreateSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotResponse.to_json())

# convert the object into a dict
create_snapshot_response_dict = create_snapshot_response_instance.to_dict()
# create an instance of CreateSnapshotResponse from a dict
create_snapshot_response_from_dict = CreateSnapshotResponse.from_dict(create_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


