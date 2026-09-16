# CancelInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_date** | **datetime** | Date of cancellation | [optional] 

## Example

```python
from pfruck_contabo.models.cancel_instance_request import CancelInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelInstanceRequest from a JSON string
cancel_instance_request_instance = CancelInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CancelInstanceRequest.to_json())

# convert the object into a dict
cancel_instance_request_dict = cancel_instance_request_instance.to_dict()
# create an instance of CancelInstanceRequest from a dict
cancel_instance_request_from_dict = CancelInstanceRequest.from_dict(cancel_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


