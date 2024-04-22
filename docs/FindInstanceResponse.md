# FindInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceResponse]**](InstanceResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_instance_response import FindInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindInstanceResponse from a JSON string
find_instance_response_instance = FindInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(FindInstanceResponse.to_json())

# convert the object into a dict
find_instance_response_dict = find_instance_response_instance.to_dict()
# create an instance of FindInstanceResponse from a dict
find_instance_response_from_dict = FindInstanceResponse.from_dict(find_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


