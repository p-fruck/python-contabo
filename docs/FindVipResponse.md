# FindVipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VipResponse]**](VipResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_vip_response import FindVipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindVipResponse from a JSON string
find_vip_response_instance = FindVipResponse.from_json(json)
# print the JSON string representation of the object
print(FindVipResponse.to_json())

# convert the object into a dict
find_vip_response_dict = find_vip_response_instance.to_dict()
# create an instance of FindVipResponse from a dict
find_vip_response_from_dict = FindVipResponse.from_dict(find_vip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


