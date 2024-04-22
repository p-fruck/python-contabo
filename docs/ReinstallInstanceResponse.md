# ReinstallInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReinstallInstanceResponseData]**](ReinstallInstanceResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.reinstall_instance_response import ReinstallInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReinstallInstanceResponse from a JSON string
reinstall_instance_response_instance = ReinstallInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(ReinstallInstanceResponse.to_json())

# convert the object into a dict
reinstall_instance_response_dict = reinstall_instance_response_instance.to_dict()
# create an instance of ReinstallInstanceResponse from a dict
reinstall_instance_response_from_dict = ReinstallInstanceResponse.from_dict(reinstall_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


