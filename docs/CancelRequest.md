# CancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status can be only set to cancelled | [optional] 

## Example

```python
from pfruck_contabo.models.cancel_request import CancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelRequest from a JSON string
cancel_request_instance = CancelRequest.from_json(json)
# print the JSON string representation of the object
print(CancelRequest.to_json())

# convert the object into a dict
cancel_request_dict = cancel_request_instance.to_dict()
# create an instance of CancelRequest from a dict
cancel_request_from_dict = CancelRequest.from_dict(cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


