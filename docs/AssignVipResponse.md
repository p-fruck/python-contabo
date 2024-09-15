# AssignVipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VipResponse]**](VipResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.assign_vip_response import AssignVipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignVipResponse from a JSON string
assign_vip_response_instance = AssignVipResponse.from_json(json)
# print the JSON string representation of the object
print(AssignVipResponse.to_json())

# convert the object into a dict
assign_vip_response_dict = assign_vip_response_instance.to_dict()
# create an instance of AssignVipResponse from a dict
assign_vip_response_from_dict = AssignVipResponse.from_dict(assign_vip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


