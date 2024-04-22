# CancelInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CancelInstanceResponseData]**](CancelInstanceResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.cancel_instance_response import CancelInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelInstanceResponse from a JSON string
cancel_instance_response_instance = CancelInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(CancelInstanceResponse.to_json())

# convert the object into a dict
cancel_instance_response_dict = cancel_instance_response_instance.to_dict()
# create an instance of CancelInstanceResponse from a dict
cancel_instance_response_from_dict = CancelInstanceResponse.from_dict(cancel_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


